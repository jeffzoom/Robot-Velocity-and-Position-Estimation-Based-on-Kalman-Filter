import numpy as np
import math
import matplotlib.pyplot as plt

# 卡尔曼滤波是不用调参的，真厉害

if __name__=="__main__":
    ## 1.设计一个匀加速直线运动，以观测此运动
    X_real = np.mat(np.zeros((2, 100))) # 空矩阵，用于存放真实状态向量
    X_real[:, 0] = np.mat([[0.0], # 初始状态向量 所有行0列    # 初位移 = 0
                           [1.0]])                       # 初速度 = 1
    a_real = 0.1 # 真实加速度
    F = np.mat([[1.0, 1.0], # 状态转移矩阵
                [0.0, 1.0]])
    Q = np.mat([[0.0001, 0.0], # 状态转移协方差矩阵，我们假设外部干扰很小
                [0.0, 0.0001]])
    B = np.mat([[0.5], # 控制矩阵
                [1.0]])
    for i in range(99):
        X_real[:, i + 1] = F * X_real[:, i] + B * a_real # 计算真实状态向量
    X_real = np.array(X_real)

    fig = plt.figure(1)
    plt.grid()
    plt.title('real displacement')
    plt.xlabel('k (s)')
    plt.ylabel('x (m)')
    plt.plot(X_real[0, :])
    plt.show()
    fig = plt.figure(2)
    plt.grid()
    plt.title('real velocity')
    plt.xlabel('k (s)')
    plt.ylabel('v (m/s)')
    plt.plot(X_real[1, :])
    plt.show()
    X_real = np.mat(X_real)

    ## 2.建立传感器观测值
    z_t = np.mat(np.zeros((2, 100)))  # 空矩阵，用于存放传感器观测值
    H = np.mat(np.zeros((2, 2))) # 观测矩阵
    H[0, 0], H[1, 1] = -1.0, -1.0
    noise = (np.mat(np.random.randn(2, 100))) # * 50  # 加入位移方差为1，速度方差为1的传感器噪声，
                       # randn函数返回一个或一组样本，具有标准正态分布。标准正态分布又是以0为均值、以1为标准差的正态分布，记为N（0，1）。
    R = np.mat([[1.0, 0.0],  # 观测噪声的协方差矩阵 ？？？ 这个R 是怎么算的，
                [0.0, 1.0]])
    R2 = np.cov(noise) # 观测噪声的协方差矩阵，我用函数，看看跟上面的R一不一样，R应该会随着noise一起变化才对
    R3 = np.cov(noise, noise)
    if (np.cov(noise) == np.cov(noise, noise)):  # 原来不一样吗
        print("true")
    else:
        print("false")

    for i in range(100):
        z_t[:, i] = H * X_real[:, i] + noise[:, i]
    z_t = np.array(z_t)

    fig = plt.figure(3)
    plt.grid()
    plt.title('sensor displacement')
    plt.xlabel('k (s)')
    plt.ylabel('x (m)')
    plt.plot(z_t[0, :])
    plt.show()
    fig = plt.figure(4)
    plt.grid()
    plt.title('sensor velocity')
    plt.xlabel('k (s)')
    plt.ylabel('v (m/s)')
    plt.plot(z_t[1, :])
    plt.show()
    z_t = np.mat(z_t)

    ## 3.执行线性卡尔曼滤波
    Q = np.mat([[0.0001, 0.0],  # 状态转移协方差矩阵，我们假设外部干扰很小，刚拿到代码的时候写的是[[1.0, 0.0],[0.0, 1.0]]
                [0.0, 0.0001]])  # 状态转移矩阵F代表了系统的动力学属性，这里F可信度很高，所以可以令Q = 0
    # 建立一系列空序列用于储存结果
    X_update = np.mat(np.zeros((2, 100)))
    P_update = np.zeros((100, 2, 2))
    X_predict = np.mat(np.zeros((2, 100)))
    P_predict = np.zeros((100, 2, 2))
    P_update[0, :, :] = np.mat([[1.0, 0.0],  # 状态向量协方差矩阵初值
                                [0.0, 1.0]])
    P_predict[0, :, :] = np.mat([[1.0, 0.0],  # 状态向量协方差矩阵初值
                                 [0.0, 1.0]])
    for i in range(99):
        # 预测
        X_predict[:, i + 1] = F * X_update[:, i] + B * a_real
        P_p = F * np.mat(P_update[i, :, :]) * F.T + Q # Q是唯一的一个自己调的参数，其实没啥可调的
        P_predict[i + 1, :, :] = P_p
        # 更新
        K = P_p * H.T * np.linalg.inv(H * P_p * H.T + R2)  # 卡尔曼增益
        P_u = P_p - K * H * P_p
        P_update[i + 1, :, :] = P_u
        X_update[:, i + 1] = X_predict[:, i + 1] + K * (z_t[:, i + 1] - H * X_predict[:, i + 1])
    X_update = np.array(X_update)
    X_real = np.array(X_real)

    fig = plt.figure(5)
    plt.grid()
    plt.title('Kalman predict displacement')
    plt.xlabel('k (s)')
    plt.ylabel('x (m)')
    plt.plot(X_real[0, :], label='real', color='b')
    plt.plot(X_update[0, :], label='predict', color='r')
    plt.legend()
    plt.show()
    fig = plt.figure(6)
    plt.grid()
    plt.title('Kalman predict velocity')
    plt.xlabel('k (s)')
    plt.ylabel('v (m/s)')
    plt.plot(X_real[1, :], label='real', color='b')
    plt.plot(X_update[1, :], label='predict', color='r')
    plt.legend()
    plt.show()
    X_update = np.mat(X_update)
    X_real = np.mat(X_real)