import ctypes
import sys

from cerver import CERVER_HANDLER_TYPE_THREADS
from cerver import cerver_set_alias
from cerver import cerver_set_receive_buffer_size
from cerver import cerver_set_thpool_n_threads
from cerver import cerver_set_handler_type
from cerver import cerver_set_reusable_address_flags
from cerver import cerver_create_web
from cerver import cerver_start, cerver_teardown, cerver_end

from cerver.http import http_cerver_get
from cerver.http import http_cerver_all_stats_print
from cerver.http import http_cerver_set_custom_data

from cerver.http import REQUEST_METHOD_GET
from cerver.http import REQUEST_METHOD_POST
from cerver.http import REQUEST_METHOD_PUT
from cerver.http import REQUEST_METHOD_DELETE
from cerver.http import HTTP_ROUTE_MODIFIER_MULTI_PART
from cerver.http import HTTP_ROUTE_AUTH_TYPE_CUSTOM
from cerver.http import http_route_create, http_cerver_route_register
from cerver.http import http_route_set_handler
from cerver.http import http_route_set_modifier
from cerver.http import http_route_child_add
from cerver.http import http_cerver_set_catch_all_route

from ermiry import *

from routes.data import *
from routes.service import *

time_service = None

# end
def end (signum, frame):
	# cerver_stats_print (time_service, False, False)
	http_cerver_all_stats_print (http_cerver_get (time_service))
	cerver_teardown (time_service)
	cerver_end ()

	ermiry_end ()

	sys.exit ("Done!")

def service_set_time_routes (http_cerver):
	# GET /api/time
	main_route = http_route_create (REQUEST_METHOD_GET, b"api/time", main_handler)
	http_cerver_route_register (http_cerver, main_route)

	# GET /api/time/version
	version_route = http_route_create (REQUEST_METHOD_GET, b"version", version_handler)
	http_route_child_add (main_route, version_route)

	# GET /api/time/data
	data_route = http_route_create (REQUEST_METHOD_GET, b"data", data_handler)
	http_route_child_add (main_route, data_route)

	# POST /api/time/data
	http_route_set_handler (data_route, REQUEST_METHOD_POST, data_update_handler)

def start ():
	global time_service
	time_service = cerver_create_web (
		b"time-service", PORT, CERVER_CONNECTION_QUEUE
	)

	# main configuration
	cerver_set_alias (time_service, b"time")

	cerver_set_receive_buffer_size (time_service, CERVER_RECEIVE_BUFFER_SIZE)
	cerver_set_thpool_n_threads (time_service, CERVER_TH_THREADS)
	cerver_set_handler_type (time_service, CERVER_HANDLER_TYPE_THREADS)

	cerver_set_reusable_address_flags (time_service, True)

	# HTTP configuration
	http_cerver = http_cerver_get (time_service)

	service_set_time_routes (http_cerver)

	# add a catch all route
	http_cerver_set_catch_all_route (http_cerver, ermiry_catch_all_handler)

	# start
	cerver_start (time_service)
