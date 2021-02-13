from apscheduler.schedulers.blocking import BlockingScheduler
from collectingData import collecting_data
from collectNewData import collecting_New_data
from tempPred import temp_Pred
from windPred import Wind_Pred
from precPred import Prec_Pred
from finalTPred import Final_Temp_Pred
from finalWPred import Final_Wind_Pred
from finalPrecPred import Final_Prec_Pred

# Create an instance of scheduler and add function.
scheduler = BlockingScheduler()
scheduler.add_job(collecting_data, trigger='cron', hour='07', minute='55')
scheduler.add_job(collecting_New_data, trigger='cron', hour='07', minute='55')
scheduler.add_job(temp_Pred, trigger='cron', hour='08', minute='00')
scheduler.add_job(Wind_Pred, trigger='cron', hour='08', minute='00')
scheduler.add_job(Prec_Pred, trigger='cron', hour='08', minute='00')
scheduler.add_job(Final_Temp_Pred, trigger='cron', hour='08', minute='01')
scheduler.add_job(Final_Wind_Pred, trigger='cron', hour='08', minute='01')
scheduler.add_job(Final_Prec_Pred, trigger='cron', hour='08', minute='01')

scheduler.start()