TIME_GAP_MINUTES = 5
MISSING_ERROR_PERCENTAGE = 0.3
VALID_GAUAGE_COUNT_LIMIT = 10

INIT_DATE_TIME_FORMAT = "%Y-%m-%d_%H:%M:%S"
UPLOADS_DEFAULT_DEST = ''
DISTRIBUTED_MODEL_TEMPLATE_DIR = ''
HECHMS_LIBS_DIR = ''
SUB_CATCHMENT_SHAPE_FILE_DIR = ''
THESSIAN_DECIMAL_POINTS = 4

OBSERVED_MYSQL_HOST = '192.168.1.43'

MYSQL_USER = 'root'
MYSQL_PASSWORD = 'cfcwm07'
MYSQL_HOST = '104.198.0.87'
MYSQL_PORT = '3306'
MYSQL_DB = 'curw'

BACK_DAYS = 2

CONFIG_ROOT = '/home/hasitha/PycharmProjects/hechms_rest_api/configs'
OUTPUT_ROOT = '/home/hasitha/PycharmProjects/hechms_rest_api/output'
#RAIN_FALL_FILE_NAME = '/home/curw/distributed_hec/OUTPUT/DailyRain-{}.csv'
RAIN_FALL_FILE_NAME = '/home/hasitha/PycharmProjects/HecHmsDistributed/output/DailyRain-{}.csv'
DISCHARGE_FILE_NAME = '/home/curw/distributed_hec/OUTPUT/DailyDischarge-{}.csv'

GAGE_MANAGER_TEMPLATE = 'Gage Manager: {MODEL_NAME}\n     Version: 4.2.1\n     Filepath Separator: \ \nEnd:'

GAGE_TEMPLATE = 'Gage: {GAGE_NAME}\n     Last Modified Date: 26 May 2018\n     Last Modified Time: 07:25:21\n' \
                '     Reference Height Units: Meters\n     Reference Height: 10.0\n     Gage Type: Precipitation\n' \
                '     Precipitation Type: Incremental\n     Units: MM\n     Data Type: PER-CUM\n     Data Source Type: Manual Entry\n' \
                '     Variant: Variant-1\n       Last Variant Modified Date: 21 May 2018\n       Last Variant Modified Time: 13:26:44\n' \
                '       Default Variant: Yes\n       DSS File Name: {MODEL_NAME}_input.dss\n' \
                '       DSS Pathname: //{GAGE_NAME}/PRECIP-INC//1HOUR/GAGE/\n       Start Time: {START_DATE}\n' \
                '       End Time: {END_DATE}\n     End Variant: Variant-1\nEnd:'

GAGE_FILE_NAME = '/home/curw/distributed_hec/distributed_model/{MODEL_NAME}.gage'

HEC_HMS_VERSION = '4.2.1'

CONTROL_TEMPLATE = 'Control: {MODEL_NAME}\n     Description: Distributed HecHms\n     Last Modified Date: {LAST_MODIFIED_DATE}\n' \
                   '     Last Modified Time: {LAST_MODIFIED_TIME}\n     Version: {HEC_HMS_VERSION}\n     Start Date: {START_DATE}\n ' \
                   '    Start Time: {START_TIME}\n     End Date: {END_DATE}\n     End Time: {END_TIME}\n     Time Interval: {TIME_INTERVAL}\n' \
                   '     Grid Write Interval: 1440\n     Grid Write Time Shift: 0\nEnd:'

CONTROL_FILE_NAME = '/home/curw/distributed_hec/distributed_model/{MODEL_NAME}.control'

RUN_FILE_TEMPLATE = 'Run: {MODEL_NAME}\n     Default Description: Yes\n     Log File: {MODEL_NAME}.log\n' \
                    '     DSS File: {MODEL_NAME}_input.dss\n' \
                    '     Last Modified Date: {LAST_MODIFIED_DATE}\n' \
                    '     Last Modified Time: {LAST_MODIFIED_TIME}\n' \
                    '     Last Execution Date: {EXECUSION_DATE}\n' \
                    '     Last Execution Time: {EXECUSION_TIME}\n' \
                    '     Basin: {MODEL_NAME}\n' \
                    '     Precip: {MODEL_NAME}\n' \
                    '     Control: {MODEL_NAME}\n' \
                    'End:'

RUN_FILE_NAME = '/home/curw/distributed_hec/distributed_model/{MODEL_NAME}.run'

HEC_HMS_HOME = '/home/curw/distributed_hec/hec-hms-421'
HEC_HMS_SH = 'hec-hms.sh'
HEC_DSSVUE_HOME = '/home/curw/distributed_hec/hec-dssvue201'
HEC_DSSVUE_SH = 'hec-dssvue.sh'
HEC_HMS_MODEL_DIR = '/home/curw/distributed_hec/distributed_model'
BASIN_STATES_DIR = 'basinStates'
HEC_EVENT = 'hec_event'
PRE_PROCESSING_SCRIPT = '/home/curw/distributed_hec/CSVTODSS.py'
POST_PROCESSING_SCRIPT = '/home/curw/distributed_hec/DSSTOCSV.py'
HEC_INPUT_DSS = '/home/curw/distributed_hec/distributed_model/{MODEL_NAME}_input.dss'
HEC_OUTPUT_DSS = '/home/curw/distributed_hec/distributed_model/{MODEL_NAME}_run.dss'
CONTROL_FILE_NAME = '/home/curw/distributed_hec/distributed_model/{MODEL_NAME}.control'
GAGE_FILE_NAME = '/home/curw/distributed_hec/distributed_model/{MODEL_NAME}.gage'
RUN_FILE_NAME = '/home/curw/distributed_hec/distributed_model/{MODEL_NAME}.run'
STATE_INDEX_NAME = HEC_EVENT + '.stateIndex'
HEC_EVENT_SCRIPT = '/home/curw/distributed_hec/distributed_model/{MODEL_NAME}.script'

