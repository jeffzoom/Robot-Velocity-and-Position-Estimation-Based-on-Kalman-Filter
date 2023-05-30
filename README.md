# Robot-Velocity-and-Position-Estimation-Based-on-Kalman-Filter
基于卡尔曼滤波的机器人速度位置估计

为了校正这种误差，我们通常会引入额外的传感器信息。例如，对上图来说，引入GPS定位信息就是一个不错的选择。这时又出现了问题：速度积分和GPS传感器包含有位置信息，那我们究竟该采信哪边的结果呢？如果两边的信息都不想浪费，该怎么把它们进行融合呢？

实际上，无论是速度积分得到的位置信息，还是GPS得到的位置信息，都存在一定的误差（GPS也存在定位精度的问题）。而在机器人的实际应用场景中，可能还存在红外、激光、视觉等更多类型的传感器，都可以以一定精度返回机器人的位置信息。那么我们该如何综合利用这些信息（传感器信息融合）来估计机器人当前的位置信息呢，这里就要用到卡尔曼滤波了。

![image](https://github.com/jeffzoom/Robot-Velocity-and-Position-Estimation-Based-on-Kalman-Filter/assets/111035313/efdec35d-4f16-4465-8938-75f404e126e7)

速度真实值

![image](https://github.com/jeffzoom/Robot-Velocity-and-Position-Estimation-Based-on-Kalman-Filter/assets/111035313/32d55d39-1b47-4553-a067-bc00b063c023)

位移真实值

![image](https://github.com/jeffzoom/Robot-Velocity-and-Position-Estimation-Based-on-Kalman-Filter/assets/111035313/8d20906d-a75a-4bfa-9352-913161a1f850)

传感器观测到的速度，与真实值相反且有噪声

![image](https://github.com/jeffzoom/Robot-Velocity-and-Position-Estimation-Based-on-Kalman-Filter/assets/111035313/1b5b3af5-32e5-47cd-9057-1109fc7fee7d)

速度卡尔曼滤波结果

![image](https://github.com/jeffzoom/Robot-Velocity-and-Position-Estimation-Based-on-Kalman-Filter/assets/111035313/10c18eba-3e72-4567-b7f7-949e23969691)

位置卡尔曼滤波结果

10个时间周期后预测值和真实值几乎一样




