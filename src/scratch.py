import utils

r = utils.Record()
log = utils.log_to_records("../logs/StarInTheCircle/caf_activation/case_0_log.json")
log_json = utils.records_to_json(log)
print(log_json)
