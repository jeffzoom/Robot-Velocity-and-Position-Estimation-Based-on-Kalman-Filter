# Robot-Velocity-and-Position-Estimation-Based-on-Kalman-Filter
基于卡尔曼滤波的机器人速度位置估计

为了校正这种误差，我们通常会引入额外的传感器信息。例如，对上图来说，引入GPS定位信息就是一个不错的选择。这时又出现了问题：速度积分和GPS传感器包含有位置信息，那我们究竟该采信哪边的结果呢？如果两边的信息都不想浪费，该怎么把它们进行融合呢？

实际上，无论是速度积分得到的位置信息，还是GPS得到的位置信息，都存在一定的误差（GPS也存在定位精度的问题）。而在机器人的实际应用场景中，可能还存在红外、激光、视觉等更多类型的传感器，都可以以一定精度返回机器人的位置信息。那么我们该如何综合利用这些信息（传感器信息融合）来估计机器人当前的位置信息呢，这里就要用到卡尔曼滤波了。

![image](https://github.com/jeffzoom/Robot-Velocity-and-Position-Estimation-Based-on-Kalman-Filter/assets/111035313/cc537ee3-ecae-4f95-8532-beefe969124b)

速度真实值

![image](https://github.com/jeffzoom/Robot-Velocity-and-Position-Estimation-Based-on-Kalman-Filter/assets/111035313/a327a103-61fd-4df2-81f6-f8ef7bfcff0f)

位移真实值

![image](https://github.com/jeffzoom/Robot-Velocity-and-Position-Estimation-Based-on-Kalman-Filter/assets/111035313/1d2c1d13-525e-47c6-9957-fdfd68d3feb4)

传感器观测到的速度，与真实值相反且有噪声

![image](https://github.com/jeffzoom/Robot-Velocity-and-Position-Estimation-Based-on-Kalman-Filter/assets/111035313/121715d8-ae63-497b-8881-72528055dfff)

速度卡尔曼滤波结果

![image](https://github.com/jeffzoom/Robot-Velocity-and-Position-Estimation-Based-on-Kalman-Filter/assets/111035313/abc32f31-c36f-4c82-90f9-dcb124a62ea7)

位置卡尔曼滤波结果

10个时间周期后预测值和真实值几乎一样




