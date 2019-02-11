from flask import Flask, request, jsonify
from flask_json import FlaskJSON, JsonError, json_response
from os import path
from datetime import datetime,timedelta
from pathlib import Path
from configs.config_data_local import UPLOADS_DEFAULT_DEST, INIT_DATE_TIME_FORMAT, RAIN_FALL_FILE_NAME, HEC_HMS_MODEL_DIR
from distributed_model.rain_fall import create_rain_files

app = Flask(__name__)
flask_json = FlaskJSON()
flask_json.init_app(app)


@app.route('/')
def hello_world():
    return 'Welcome to HecHms(Distributed) Server!'


@app.route('/HECHMS/distributed/init-model', methods=['GET', 'POST'])
@app.route('/HECHMS/distributed/init-model/<string:run_datetime>',  methods=['GET', 'POST'])
@app.route('/HECHMS/distributed/init-model/<string:run_datetime>/<int:back_days>/<int:forward_days>',  methods=['GET', 'POST'])
def prepare_input_files(run_datetime=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), back_days=2, forward_days=3):
    print('prepare_input_files.')
    print('run_datetime : ', run_datetime)
    print('back_days : ', back_days)
    print('forward_days : ', forward_days)
    run_datetime = datetime.strptime(run_datetime, '%Y-%m-%d %H:%M:%S')
    to_date = run_datetime + timedelta(days=forward_days)
    from_date = run_datetime - timedelta(days=back_days)
    file_date = run_datetime.strftime('%Y-%m-%d')
    from_date = from_date.strftime('%Y-%m-%d %H:%M:%S')
    to_date = to_date.strftime('%Y-%m-%d %H:%M:%S')
    file_name = RAIN_FALL_FILE_NAME.format(file_date)
    print('file_name : ', file_name)
    print('{from_date, to_date} : ', {from_date, to_date})
    try:
        create_rain_files(file_name, run_datetime.strftime('%Y-%m-%d %H:%M:%S'), forward_days, back_days)
        # rain_fall_file = Path(file_name)
        # if rain_fall_file.is_file():
        #     create_gage_file_by_rain_file('distributed_model', file_name)
        #     create_control_file_by_rain_file('distributed_model', file_name)
        # else:
        #     create_gage_file('distributed_model', from_date, to_date)
        #     create_control_file('distributed_model', from_date, to_date)
        # create_run_file('distributed_model', run_datetime.strftime('%Y-%m-%d %H:%M:%S'))
        return json_response(status_=200, description='Successfully created input files.')
    except Exception as e:
        print(e)
        raise JsonError(status_=400, description='Input file creation error.')


@app.route('/HECHMS/distributed/pre-process', methods=['GET', 'POST'])
@app.route('/HECHMS/distributed/pre-process/<string:run_datetime>',  methods=['GET', 'POST'])
def pre_processing(run_datetime=datetime.now().strftime('%Y-%m-%d %H:%M:%S')):
    print('pre_processing.')
    print('run_datetime : ', run_datetime)
    run_datetime = datetime.strptime(run_datetime, '%Y-%m-%d %H:%M:%S')
    ret_code = 0#execute_pre_dssvue('distributed_model', run_datetime.strftime('%Y-%m-%d %H:%M:%S'))
    if ret_code == 0:
        return jsonify({'Result': 'Success'})
    else:
        return jsonify({'Result': 'Fail'})


@app.route('/HECHMS/distributed/run-model', methods=['GET', 'POST'])
def run_hec_hms_model():
    print('run_hec_hms_model.')
    ret_code = 0#execute_hechms('distributed_model', HEC_HMS_MODEL_DIR)
    if ret_code == 0:
        return jsonify({'Result': 'Success'})
    else:
        return jsonify({'Result': 'Fail'})


@app.route('/HECHMS/distributed/post-process', methods=['GET', 'POST'])
@app.route('/HECHMS/distributed/post-process/<string:run_datetime>',  methods=['GET', 'POST'])
def post_processing(run_datetime=datetime.now().strftime('%Y-%m-%d %H:%M:%S')):
    print('post_processing.')
    print('run_datetime : ', run_datetime)
    run_datetime = datetime.strptime(run_datetime, '%Y-%m-%d %H:%M:%S')
    ret_code = 0#execute_post_dssvue('distributed_model', run_datetime.strftime('%Y-%m-%d %H:%M:%S'))
    if ret_code == 0:
        return jsonify({'Result': 'Success'})
    else:
        return jsonify({'Result': 'Fail'})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

