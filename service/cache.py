import traceback
from typing import Any

import redis

from cerver.utils import cerver_log_success, cerver_log_error

redis_pool = None
redis_client = None

def ermiry_cache_init ():
	global redis_pool
	global redis_client

	result = False

	try:
		redis_pool = redis.ConnectionPool (
			host="redis", port=6379, decode_responses=True
		)

		redis_client = redis.StrictRedis (
			connection_pool=redis_pool,
			socket_connect_timeout=1
		)

		redis_client.ping ()

		cerver_log_success (
			b"Redis Cache connected!"
		)

		result = True

	except Exception as e:
		cerver_log_error (
			b"Error connecting to Redis Cache!"
		)

		print (e)

	return result

def ermiry_cache_get_test ():
	result = None

	try:
		result = redis_client.get ("oki")
	except:
		cerver_log_error (b"Failed to get cache test!")

	return result

def ermiry_cache_set_test ():
	result = False

	try:
		redis_client.set ("oki", "doki")
		result = True
	except:
		cerver_log_error (b"Failed to set cache test!")

	return result

def ermiry_cache_get (value: str):
	result = None

	try:
		result = redis_client.get (value)
	except:
		cerver_log_error (b"Failed to get cache value!")

	return result

def ermiry_cache_set (key: str, value: Any):
	result = None

	try:
		result = redis_client.set (key, value)
	except:
		cerver_log_error (b"Failed to set value!")

	return result

def ermiry_cache_get_multiple (values: list):
	result = None

	try:
		result = redis_client.mget (values)
	except:
		cerver_log_error (b"Failed to get multiple cache values!")

	return result

def ermiry_cache_hgetall (key: str):
	result = None

	try:
		result = redis_client.hgetall (key)
	except:
		cerver_log_error (b"Failed to get all values from hash!")

	return result

def ermiry_cache_hmset (key: str, values: dict):
	result = None

	try:
		result = redis_client.hmset (key, values)
	except:
		cerver_log_error (b"Failed to set multiple hash values!")

	return result

def ermiry_cache_scan (match: str):
	result = None

	try:
		result = redis_client.scan_iter (match)
	except:
		cerver_log_error (b"Failed to perform scan!")

	return result

def ermiry_cache_push_to_queue (queue: str, data: str):
	try:
		redis_client.rpush (queue, data)
	except:
		cerver_log_error (b"Failed to push to queue!")

def ermiry_cache_is_set_member (set_name: str, value: str):
	result = False

	try:
		result = redis_client.sismember (set_name, value)
	except:
		cerver_log_error (b"Failed to check set member!")

	return result

def ermiry_cache_add_set_member (set_name: str, value: str):
	try:
		redis_client.sadd (set_name, value)
	except:
		cerver_log_error (b"Failed to add member to set!")

def ermiry_cache_remove_set_member (set_name: str, value: str):
	try:
		redis_client.srem (set_name, value)
	except:
		cerver_log_error (b"Failed to remove member from set!")

def ermiry_cache_ts_range (ts_name: str, start: int, end: int):
	result = None

	try:
		result = redis_client.ts ().range (ts_name, start, end)
	except:
		traceback.print_exc ()
		cerver_log_error (b"Failed to execute timeseries range!")

	return result

def ermiry_cache_ts_incrby (ts_name: str, value: int):
	try:
		redis_client.ts ().incrby (ts_name, value)
	except:
		traceback.print_exc ()
		cerver_log_error (b"Failed to increment timeseries!")
