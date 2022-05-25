import ctypes

from cerver.http import HTTP_STATUS_OK
from cerver.http import http_response_json_custom_reference_send

from errors import SERVICE_ERROR_NONE
from errors import service_error_send

from controllers.data import data_fetch
from controllers.data import data_update

# GET /api/time/data
@ctypes.CFUNCTYPE (None, ctypes.c_void_p, ctypes.c_void_p)
def data_handler (http_receive, request):
	error, result = data_fetch ()

	if (error == SERVICE_ERROR_NONE):
		actual_result = result.encode ("utf-8")
		http_response_json_custom_reference_send (
			http_receive, HTTP_STATUS_OK,
			actual_result, len (actual_result)
		)

	else:
		service_error_send (error, http_receive)

# POST /api/time/data
@ctypes.CFUNCTYPE (None, ctypes.c_void_p, ctypes.c_void_p)
def data_update_handler (http_receive, request):
	service_error_send (data_update (), http_receive)
