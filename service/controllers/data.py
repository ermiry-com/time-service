import datetime
import json

from cache import ermiry_cache_ts_range
from cache import ermiry_cache_ts_add
from cache import ermiry_cache_ts_incrby
from errors import SERVICE_ERROR_NONE
from errors import SERVICE_ERROR_SERVER_ERROR

def data_fetch ():
	error = SERVICE_ERROR_NONE
	result = None

	try:
		now = datetime.datetime.utcnow ()
		start = now - datetime.timedelta (days=1)
		end = now + datetime.timedelta (days=1)

		real_start = int (start.timestamp () * 1000)
		real_end = int (end.timestamp () * 1000)

		print (real_start, real_end)

		data = ermiry_cache_ts_range ("todo:data", real_start, real_end)

		if (data is None):
			data = []

		real_data = []
		for point in data:
			real_data.append ({
				"time": point[0],
				"value": point[1]
			})

		result = json.dumps (real_data)
		print (result)
	except:
		error = SERVICE_ERROR_SERVER_ERROR

	return error, result

def data_update ():
	error = SERVICE_ERROR_NONE

	ermiry_cache_ts_add ("todo:data", 1)

	return error
