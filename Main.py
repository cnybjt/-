from BLL.RealtimeData import RealtimeData


# import schedule

def run_realtime():

    send_data = RealtimeData()
    # 处理G_Data数据
    send_data.deal_realtime_data()



    # dfdata=calcall.read_Data_Test()
    # cnm = RedisHelper()
    # cnm.push_data_to_redis(dfdata,'GD')
# def calc_rate():
#     calc_select_rate = CalcSelectRate()
#     calc_select_rate.data_process()


if __name__ == '__main__':
    # setting = Config.Config()
    # RepeatTime = setting.RepeatCycle
    # # schedule.every(RepeatTime).seconds.do(run_realtime)
    # schedule.every(RepeatTime).hours.do(run_realtime)
    # # schedule.every().day.at("21:30").do(run_realtime)
    #
    # while True:
    #     schedule.run_pending()


    run_realtime()

