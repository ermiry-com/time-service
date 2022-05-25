# Ermiry Demo Time Service

### Development
```
sudo docker run \
  -it \
  --name time --rm \
  -p 5001:5001 --net ermiry \
  -v /home/ermiry/Documents/projects/time-service:/home/time \
  -e RUNTIME=development \
  -e PORT=5001 \
  -e CERVER_RECEIVE_BUFFER_SIZE=4096 -e CERVER_TH_THREADS=4 \
  -e CERVER_CONNECTION_QUEUE=4 \
  ermiry/time-service:development /bin/bash
```

## Routes

### Main

#### GET /api/time
**Access:** Public \
**Description:** Time top level route \
**Returns:**
  - 200 on success

#### GET /api/time/version
**Access:** Public \
**Description:** Returns time service current version \
**Returns:**
  - 200 and version's json on success
