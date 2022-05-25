import datetime
import json

from cache import ermiry_cache_ts_range
from cache import ermiry_cache_ts_incrby
from errors import SERVICE_ERROR_NONE

def data_fetch ():
	error = SERVICE_ERROR_NONE

	now = datetime.datetime.utcnow ()
	start = now - datetime.timedelta (days=1)
	end = now + datetime.timedelta (days=1)

	real_start = int (start.timestamp () * 1000)
	real_end = int (end.timestamp () * 1000)

	print (real_start, real_end)

	data = ermiry_cache_ts_range ("todo:data", real_start, real_end)

	if (data is None):
		data = []

	result = json.dumps (data)
	print (result)

	return error, result

def data_update ():
	error = SERVICE_ERROR_NONE

	ermiry_cache_ts_incrby ("todo:data", 1)

	return error
