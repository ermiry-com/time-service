import os

from cache import ermiry_cache_hmset
from errors import service_errors_end
from runtime import *
from version import service_version

RUNTIME = runtime_from_string (os.environ.get ("RUNTIME"))

PORT = int (os.environ.get ("PORT"))

CERVER_RECEIVE_BUFFER_SIZE = int (os.environ.get ("CERVER_RECEIVE_BUFFER_SIZE"))
CERVER_TH_THREADS = int (os.environ.get ("CERVER_TH_THREADS"))
CERVER_CONNECTION_QUEUE = int (os.environ.get ("CERVER_CONNECTION_QUEUE"))

def ermiry_config ():
	print ("RUNTIME: ", runtime_to_string (RUNTIME))

	print ("PORT: ", PORT)

	print ("CERVER_RECEIVE_BUFFER_SIZE: ", CERVER_RECEIVE_BUFFER_SIZE)
	print ("CERVER_TH_THREADS: ", CERVER_TH_THREADS)
	print ("CERVER_CONNECTION_QUEUE: ", CERVER_CONNECTION_QUEUE)

def ermiry_init ():
	# web:service_name:state
	ermiry_cache_hmset (
		"web:time:state",
		{
			"runtime": runtime_to_string (RUNTIME),
			"port": PORT,
			"cerver_receive_buffer_size": CERVER_RECEIVE_BUFFER_SIZE,
			"cerver_th_threads": CERVER_TH_THREADS,
			"cerver_connection_queue": CERVER_CONNECTION_QUEUE
		}
	)

	# web:service_name:version
	ermiry_cache_hmset (
		"web:time:version", service_version
	)

def ermiry_end ():
	service_errors_end ()
