# import a
from a import *
if __name__ == '__main__':
    
    servo_id = 0
    # b3m = serial.Serial('COM6', baudrate=9600,parity=serial.PARITY_NONE, timeout=2)
    ###毎回これやる################################
    reData = B3M_Write_CMD(0x00, 0x02, 0x28)
    time.sleep(0.1)
    #位置制御モードに設定 (角度を指定して動作するモードです)
    reData = B3M_Write_CMD(0x00, 0x02, 0x28)
    time.sleep(0.1)
    # 軌道生成タイプ：Even (直線補間タイプの位置制御を指定)
    reData = B3M_Write_CMD(0x00, 0x01, 0x29)
    time.sleep(0.1)
    # ゲインプリセット：No.0 (PIDのプリセットゲインを位置制御モード用に設定)
    reData = B3M_Write_CMD(0x00, 0x00, 0x5C)
    time.sleep(0.1)
    # 動作モード：Normal （Freeの状態からトルクオン）
    reData = B3M_Write_CMD(0x00, 0x00, 0x28)
    ################################################
    print('セットアップ完了')

    for i in range(10):
        reData = B3M_setPos(0, 5000, 500)
        time.sleep(1)
        reData = B3M_setPos(0, -5000, 500)
        time.sleep(1)
        reData = B3M_setPos(0, 0, 500)
        time.sleep(1)
    b3m.close()
