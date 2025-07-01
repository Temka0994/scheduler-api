# SchedulerApi
This project was made to support email-notification-api. The project is using FastAPI as a backend framework and MongoDB as a database management system.
# Techonology Stack
- Python 3.11;
- FastAPI;
- Motor;
- Pydantic;
- HTTPX;
# How to use it
### Clone repository
Firstly, the project should be cloned using the following command in the console:
```bash
git clone https://github.com/Temka0994/scheduler-api.git
```
After this navigate to the scheduler-api folder:
```bash
cd schedulerAPI
```

### Requirements
Additionally, all the requirements should be downloaded using the following command:
```bash
pip install -r requirements.txt
```

### Database
First and last ste[ is to change the database path. This should be done by opening the [database.py](./src/database.py) file and inserting the desired path into the `DATABASE_URL` field.


### Final step
After this you can run the Scheduler application with the command:
```bash 
uvicorn src.main:app --reload --port 8001
```
