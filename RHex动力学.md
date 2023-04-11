# 课程内工作

## 内容

### 雅可比矩阵

1. 不同类型的函数

    > 矩阵求导相关：https://zhuanlan.zhihu.com/p/263777564
    >
    > 1. **$f$是标量**
    >
    >     > **把各个元素取出来运算，像编程时函数传入的参数**
    >     >
    >     > **返回一个值**
    >
    >     1. $f(x)$，输入标量，返回标量
    >
    >         > $f(x)=x+2$
    >
    >     2. $f(\bold x)$，输入向量，返回标量
    >
    >         > $x=[x_1,x_2,x_3]$
    >         >
    >         > $f(\bold x)=x_1+x_2+x_3$
    >
    >     3. $f(\bold X)$，输入矩阵，返回标量
    >
    >         > $\bold X=\begin{bmatrix}x_1&x_2\\x_3 & x_4\end{bmatrix}$
    >         >
    >         > $f(\bold X)=x_1+x_2+x_3+x_4$
    >
    > 2. $\bold f$**是向量**
    >
    >     > **把各个元素取出来运算**
    >     >
    >     > **返回值是多个，每一个返回值都对应一种对所有传入参数的运算，排列成一个向量返回**
    >
    >     1. $\bold f(x)$，输入标量，返回向量
    >
    >         > $\bold f(x)=\begin{bmatrix}g_1(x)\\g_2(x)\\g_3(x)\end{bmatrix}=\begin{bmatrix}x+1\\x+2\\x+3\end{bmatrix}$
    >
    >     2. $\bold f(\bold x)$，输入向量，返回向量
    >
    >         > $\bold f(\bold x)=\begin{bmatrix}g_1(\bold x)\\g_2(\bold x)\\g_3(\bold x)\end{bmatrix}=\begin{bmatrix}g_1(x_1,x_2)\\g_2(x_1,x_2)\\g_3(x_1,x_2)\end{bmatrix}=\begin{bmatrix}x_1+x_2\\x_1-x_2\\-x_1+x_2\end{bmatrix}$
    >
    >     3. $\bold f(\bold X)$，输入矩阵，返回向量
    >
    >         > $\bold f(\bold X)=\begin{bmatrix}g_1(\bold X)\\g_2(\bold X)\\g_3(\bold X)\end{bmatrix}=\begin{bmatrix}g_1(\begin{bmatrix}x_1&x_2\\x_3 & x_4\end{bmatrix})\\g_2(\begin{bmatrix}x_1&x_2\\x_3 & x_4\end{bmatrix})\\g_3(\begin{bmatrix}x_1&x_2\\x_3 & x_4\end{bmatrix})\end{bmatrix}=\begin{bmatrix}x_1+x_2-x_3+x_4\\x_1-x_2+x_3+x_4\\x_1+x_2+x_3-x_4\end{bmatrix}$
    >
    > 3. $\bold F$**是矩阵**
    >
    >     > **把各个元素取出来运算**
    >     >
    >     > **返回值是多个，每一个返回值都对应一种对所有传入参数的运算，排列成一个矩阵返回**

2. 机器人学的关节空间和笛卡尔空间

    > Modern Robotics chap. 2

    1. 关节空间其实是分析力学里的广义坐标。常见的都是旋转关节，于是取旋转的角度作为坐标。几个自由度就有几个坐标，自由度的概念不在这里写了。常见的串联开环机械臂中有几个旋转R关节就是有几个自由度。

    2. 常见的串联开环机械臂，已知关节空间坐标（各个旋转R关节角度），求末端的笛卡尔空间坐标，是运动学正解

        > $\bold x=\bold f(\bold \theta)$，输入向量，返回向量
        >
        > $\begin{bmatrix}x\\y\\z\end{bmatrix}=\bold f(\theta_1,\theta_2,...,\theta_n)=\begin{bmatrix}g_1(\theta_1,\theta_2,...,\theta_n)\\g_2(\theta_1,\theta_2,...,\theta_n)\\g_3(\theta_1,\theta_2,...,\theta_n)\end{bmatrix}$

    3. 两边对时间求导，可以得到速度关系

        > $\begin{bmatrix}\dot x\\\dot y\\\dot z\end{bmatrix}=\frac{d\bold f(\theta_1,\theta_2,...,\theta_n)}{dt}=\begin{bmatrix}\frac{dg_1(\theta_1,\theta_2,...,\theta_n)}{dt}\\\frac{dg_2(\theta_1,\theta_2,...,\theta_n)}{dt}\\\frac{dg_3(\theta_1,\theta_2,...,\theta_n)}{dt}\end{bmatrix}$
        >
        > 其中$\dot x=\frac{dx}{dt}$
        >
        > 求全微分：
        >
        > 
        >
        > $\begin{bmatrix}\dot x\\\dot y\\\dot z\end{bmatrix}=\begin{bmatrix}\frac{\frac{\partial g_1}{\partial \theta_1}d\theta_1+\frac{\partial g_1}{\partial \theta_2}d\theta_2+...+\frac{\partial g_1}{\partial \theta_n}d\theta_n}{dt}\\\frac{\frac{\partial g_2}{\partial \theta_1}d\theta_1+\frac{\partial g_2}{\partial \theta_2}d\theta_2+...+\frac{\partial g_2ß}{\partial \theta_n}d\theta_n}{dt}\\\frac{\frac{\partial g_3}{\partial \theta_1}d\theta_1+\frac{\partial g_3}{\partial \theta_2}d\theta_2+...+\frac{\partial g_3}{\partial \theta_n}d\theta_n}{dt}\end{bmatrix}$
        >
        > $\begin{bmatrix}\dot x\\\dot y\\\dot z\end{bmatrix}=\begin{bmatrix}\frac{\partial g_1}{\partial\theta_1} & \frac{\partial g_1}{\partial\theta_2} & ... &\frac{\partial g_1}{\partial\theta_n}\\\frac{\partial g_2}{\partial\theta_1} & \frac{\partial g_2}{\partial\theta_2} & ... &\frac{\partial g_2}{\partial\theta_n}\\\frac{\partial g_3}{\partial\theta_1} & \frac{\partial g_3}{\partial\theta_2} & ... &\frac{\partial g_3}{\partial\theta_n}\end{bmatrix}\begin{bmatrix}\dot\theta_1\\\dot\theta_2\\\vdots\\\dot\theta_n\end{bmatrix}$
        >
        > $\begin{bmatrix}\dot x\\\dot y\\\dot z\end{bmatrix}=\bold J\begin{bmatrix}\dot\theta_1\\\dot\theta_2\\\vdots\\\dot\theta_n\end{bmatrix}$

    4. 不光是关节坐标满足这样，任何广义坐标都可以这样。雅可比矩阵换成相应的导数即可

    5. 补充一个我老是搞不清的乘法区别：

        > https://zhuanlan.zhihu.com/p/79760117

        1. 矩阵乘法

            1. 矩阵乘积(Matrix Product, Matmul Product)

            2. Hadamard Product, Element-wise Product：对应位相乘

                $\begin{bmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{bmatrix}\odot\begin{bmatrix}b_{11}&b_{12}\\b_{21}&b_{22}\end{bmatrix}=\begin{bmatrix}a_{11}b_{11}&a_{12}b_{12}\\a_{21}b_{21}&a_{22}b_{22}\end{bmatrix}$

                > \odot$\to\odot$

            3. （不管这个）

        2. 向量乘法

            1. 点积/内积(Inner Product, Dot Product)：对应位相乘

                $a=(a_1,a_2,...,a_n)$

                $b=(b_1,b_2,...,b_n)$

                $a\cdot b=(a_1b_1,a_2b_2,...,a_nb_n)$

            2. 外积(Outer Product)：笛卡尔积，组合，结果是矩阵

                $a=(a_1,a_2,...,a_m)$

                $b=(b_1,b_2,...,b_n)$

                $a\otimes b=\begin{bmatrix}a_1b_1&a_1b_2&\cdots&a_1b_n\\a_2b_1&a_2b_2&\cdots&a_2b_n\\\vdots&\vdots&\ddots&\vdots\\a_mb_1&a_mb_2&\cdots&a_mb_n\end{bmatrix}$

                > \otimes$\to\otimes$
                >
                > \cdots$\to\cdots$
                >
                > \vdots$\to\vdots$
                >
                > \ddots$\to\ddots$

            3. 叉积(Cross Product)

3. 机器人Minitaur五连杆正运动学求解

    ![image-20210904220422224](RHex%E5%8A%A8%E5%8A%9B%E5%AD%A6.assets/image-20210904220422224-0830588.png)<img src="RHex%E5%8A%A8%E5%8A%9B%E5%AD%A6.assets/image-20210904220405369-0830592.png" alt="image-20210904220405369" style="zoom:50%;" />

    在进行验算时，我发现了他们这篇论文的两个错误：

    1. 当$\beta>\pi$时，式(8)和式(9)的第二个负号要变成正号
    2. 式(10)的A项和D项均少乘了$\sin\beta$，并且D项中的最后一个根号里也是不对的

4. 我们的机器人RHex-T3求解

    > 解算部分不方便放出来，请老师见谅

    1. 这一部分我用好几种方法推了很多页，最后发现用Minitaur方法是结果上看最简单的。因为在实际上运用雅可比的时候是需要实时计算的，并且是需要在嵌入式系统上进行的，对算力有限制，所以应该要简单一点。

    2. 验算部分

        <img src="RHex%E5%8A%A8%E5%8A%9B%E5%AD%A6.assets/image-20210904221233832-0830594.png" alt="image-20210904221233832" style="zoom:50%;" />

5. 雅可比除了速度关系，还联系了力的关系

    > https://zhuanlan.zhihu.com/p/341806737

    1. 已知、约定

        1. $\begin{bmatrix}\dot x\\\dot y\\\dot z\\\dot\alpha\\\dot\beta\\\dot\gamma\end{bmatrix}=\bold J\begin{bmatrix}\dot\theta_1\\\dot\theta_2\\\vdots\\\dot\theta_n\end{bmatrix}$

            $\bold{\dot x}=\bold J \bold{\dot\theta}$

        2. 关节扭矩：$\tau=\begin{bmatrix}\tau_1\\\tau_2\\\vdots\\\tau_n\end{bmatrix}$

        3. 末端力与扭矩：$F=\begin{bmatrix}f_1\\f_2\\f_3\\n_1\\n_2\\n_3\end{bmatrix}$

    2. 末端功率和关节功率相等，功率=力*速度

        1. 末端：$P=F^T\bold{\dot x}=F^T(\bold J\dot\theta)$

            > 两个乘法都是矩阵乘法，功率是标量

        2. 关节：$P=\tau^T\dot\theta$

        3. 相等：

            > $F^T(\bold J\dot\theta)=\tau^T\dot\theta$
            >
            > $F^T\bold J=\tau^T$
            >
            > $\bold J^TF=\tau$

### 分析力学中的拉格朗日方程推导

1. 随便记一点我之前弄混的约定

    1. $\dot{x}=\frac{dx}{dt}$，其他类似

2. 力学系统

    1. 一个质点可在空间中随便动
    2. 两个质点构成一个刚体，刚体有形状，一个质点乱动的时候，形状限制了另一个质点的位置
    3. 这个限制就是个约束
    4. 有这种约束的系统就是力学系统？

3. 约束

    1. 约束力不做功，像单摆和一些轨道给的力，只是限制运动方向。比如两个小球用一个连杆连在一起，推动一个小球，这这个小球会通过连杆拉另一个小球。连杆和球之间的力就是约束力
    2. 约束力不做功，叫理想约束
    3. 方程，隐式表达
    4. 质点受力，除了约束力就是主动力

4. 广义坐标

    1. 可以把隐式表达变成显式
    2. 显式表示后，坐标维数=自由度个数
    3. 设有$n$个广义坐标$q_s(s=1,...,n)$，刚体中有$N$个质点，第$i$个质点的坐标：$\overrightarrow{r_i}=\overrightarrow{r}(q_1,q_2,...,q_n,t)$

5. 虚位移

    1. 方向任意，要动又没动，无穷小
    2. 符号：$\delta\overrightarrow{r}$
    3. $\delta$可以看成就是$d$

6. 虚功原理

7. 达朗贝尔原理

    1. 力学系统所受理想约束力的总虚功为零
    2. $\sum\limits_{i=0}^{N}(\overrightarrow{F_i}-m\ddot{\overrightarrow{r}})\cdot\delta\overrightarrow{r_i}=0$
    3. 推导
        1. 对于每个质点：$\overrightarrow{F_i}+\overrightarrow{N_i}=m\ddot{\overrightarrow{r_i}}$，其中$\overrightarrow{N_i}$是约束力。对于每个质点，约束力和主动力就是一个质点收到的力，等于ma，牛二
        2. 左右乘虚位移：$\overrightarrow{F_i}\cdot\delta\overrightarrow{r}+\overrightarrow{N_i}\cdot\delta\overrightarrow{r}=m\ddot{\overrightarrow{r}}\cdot\delta\overrightarrow{r_i}$
        3. 因为是理想约束，所以总的$\Sigma\overrightarrow{N_i}\cdot\delta\overrightarrow{r}=0$。就看刚刚那个例子，两小球加个杆，杆子给的约束力，合计上不做功
    4. 说明
        1. 如果系统没有约束，每个i点都是自由的质点，那么$\overrightarrow{N_i}$为0，因为不受约束力，并且$\overrightarrow{F_i}-m\ddot{\overrightarrow{r}}=0$，因为这就是牛二，$\overrightarrow{F_i}$就是每个质点的外力
        2. 如果有约束，则每个$\delta\overrightarrow{r_i}$不是独立的，因为约束力限制了他们的运动，一个质点虚位移往左，那么约束力会拉动周围的东西也往左（或者别的方向，总之是有限制）

8. 拉格朗日方程

    1. 方程，$(s=1,2,3,...,n)$

        1. $Q_s=\frac{d(\frac{\partial T}{\partial \dot{q_s}})}{dt}-\frac{\partial T}{\partial q_s}$

        2. $Q_s=\frac{dP_s}{dt}-\frac{\partial T}{\partial q_s}$

        3. $0=\frac{d(\frac{\partial (L)}{\partial \dot{q_s}})}{dt}-\frac{\partial (L)}{\partial q_s}$

        4. $f=\frac{d(\frac{\partial (L)}{\partial \dot{q_s}})}{dt}-\frac{\partial (L)}{\partial q_s}$，$f$是外力

        5. 其中：

            1. 广义力：$Q_s=\sum\limits_{i=0}^{N}（\overrightarrow{F_i}\cdot\frac{\partial\overrightarrow{r_i}}{\partial q_s}）$

                > 力分解到每个坐标的方向上再合起来

            2. 广义动量：$P_s=\frac{\partial T}{\partial \dot{q_s}}$

                > 动能对广义速度求偏导

            3. 动能：$T=\sum\limits_{i=0}^{N}\frac{1}{2}m_i\dot{\overrightarrow{r_i}}^2$

    2. 就是从这个达朗贝尔原理的公式推来的：$\sum\limits_{i=0}^{N}(\overrightarrow{F_i}-m\ddot{\overrightarrow{r}})\cdot\delta\overrightarrow{r_i}=0$

    3. 推导：

        1. $\delta\overrightarrow{r_i}$

            1. $\overrightarrow{r_i}=\overrightarrow{r}(q_1,q_2,...,q_n,t)$

            2. 全微分，在这里，求全微分是为了找$q$和达朗贝尔原理式子的关系，为了消去约束（为了2.4）：

                $d\overrightarrow{r_i}=\sum\limits_{s=1}^{n}(\frac{\partial\overrightarrow{r_i}}{\partial q_s}\cdot dq_s)+\frac{\partial\overrightarrow{r_i}}{\partial t}\cdot dt$

                > 求解全微分的意义？最好感性一点的认识 - xingpz2008的回答 - 知乎 https://www.zhihu.com/question/31464934/answer/735165677

            3. $\delta$可以看成就是$d$：

                $\delta\overrightarrow{r_i}=\sum\limits_{s=1}^{n}(\frac{\partial\overrightarrow{r_i}}{\partial q_s}\cdot \delta q_s)+\frac{\partial\overrightarrow{r_i}}{\partial t}\cdot \delta t$

            4. 对于当前时刻进行分析（虚位移），则第二项为0：

                $\delta\overrightarrow{r_i}=\sum\limits_{s=1}^{n}(\frac{\partial\overrightarrow{r_i}}{\partial q_s}\cdot \delta q_s)$

            5. 代入到达朗贝尔原理的公式：

                $\sum\limits_{i=0}^{N}[(\overrightarrow{F_i}-m\ddot{\overrightarrow{r}})\cdot\sum\limits_{s=1}^{n}(\frac{\partial\overrightarrow{r_i}}{\partial q_s}\cdot \delta q_s)]=0$

        2. 整理

            1. $\sum\limits_{i=0}^{N}[(\overrightarrow{F_i}-m\ddot{\overrightarrow{r}})\cdot\sum\limits_{s=1}^{n}(\frac{\partial\overrightarrow{r_i}}{\partial q_s}\cdot \delta q_s)]=0$

            2. 拆开括号：

                $\sum\limits_{i=0}^{N}[\overrightarrow{F_i}\cdot\sum\limits_{s=1}^{n}(\frac{\partial\overrightarrow{r_i}}{\partial q_s}\cdot \delta q_s)-m\ddot{\overrightarrow{r}}\cdot\sum\limits_{s=1}^{n}(\frac{\partial\overrightarrow{r_i}}{\partial q_s}\cdot \delta q_s)]=0$

            3. 换加号位置

                $\sum\limits_{s=1}^{n}[\sum\limits_{i=0}^{N}[(\overrightarrow{F_i}\cdot\frac{\partial\overrightarrow{r_i}}{\partial q_s}）-（m\ddot{\overrightarrow{r_i}}\cdot\frac{\partial\overrightarrow{r_i}}{\partial q_s})]\cdot \delta q_s]=0$

            4. 因为$\delta q_s$是广义坐标了，显式表示了，之间是独立的，独立的那么每一点的在这个坐标下的约束力是不存在的，所以外力等于F，直接牛二，所以：

                $\sum\limits_{i=0}^{N}[(\overrightarrow{F_i}-m_i\ddot{\overrightarrow{r_i}})\cdot\frac{\partial\overrightarrow{r_i}}{\partial q_s}]=0$

        3. 式2.4第一项，设为$Q_s$

            1. $Q_s=\sum\limits_{i=0}^{N}（\overrightarrow{F_i}\cdot\frac{\partial\overrightarrow{r_i}}{\partial q_s}）$
            2. $Q_s$为**广义力**

        4. 式2.4第二项

            1. $\sum\limits_{i=0}^{N}（m\ddot{\overrightarrow{r_i}}\cdot\frac{\partial\overrightarrow{r_i}}{\partial q_s})$

            2. 利用乘法求导的公式，联系动能$T=\sum\limits_{i=0}^{N}\frac{1}{2}m_i\dot{\overrightarrow{r_i}}^2$

                1. $\frac{df\cdot g}{dt}=f\cdot\frac{dg}{dt}+\frac{df}{dt}\cdot g$
                2. $\frac{df}{dt}\cdot g=\frac{df\cdot g}{dt}-f\cdot\frac{dg}{dt}$
                3. $\sum\limits_{i=0}^{N}（m\ddot{\overrightarrow{r}}\cdot\frac{\partial\overrightarrow{r_i}}{\partial q_s})=[\frac{d(\sum\limits_{i=0}^{N}m_i\dot{\overrightarrow{r_i}}\cdot \frac{\partial\overrightarrow{r_i}}{\partial q_s})}{dt}]-\sum\limits_{i=0}^{N}(m_i\dot{\overrightarrow{r_i}}\cdot \frac{d(\frac{\partial \overrightarrow{r_i}}{\partial q_s})}{dt})$

            3. **拉格朗日关系**

                1. $\frac{\partial\overrightarrow{r_i}}{\partial q_s}=\frac{\partial\dot{\overrightarrow{r_i}}}{\partial \dot{q_s}}$

                2. $\frac{d(\frac{\partial\overrightarrow{r_i}}{\partial q_s})}{dt}=\frac{\partial(\frac{d\overrightarrow{r_i}}{dt})}{\partial q_s}$

                3. 代入到4.2.3中：

                    $\sum\limits_{i=0}^{N}（m\ddot{\overrightarrow{r}}\cdot\frac{\partial\overrightarrow{r_i}}{\partial q_s})=[\frac{d(\sum\limits_{i=0}^{N}m_i\dot{\overrightarrow{r_i}}\cdot \frac{\partial\dot{\overrightarrow{r_i}}}{\partial \dot{q_s}})}{dt}]-\sum\limits_{i=0}^{N}(m_i\dot{\overrightarrow{r_i}}\cdot \frac{\partial(\frac{d\overrightarrow{r_i}}{dt})}{\partial q_s})$

            4. 联系动能$T=\sum\limits_{i=0}^{N}\frac{1}{2}m_i\dot{\overrightarrow{r_i}}^2$，求导链式法则凑出：

                $\sum\limits_{i=0}^{N}（m\ddot{\overrightarrow{r}}\cdot\frac{\partial\overrightarrow{r_i}}{\partial q_s})=\frac{d(\frac{\partial(\sum\limits_{i=0}^{N}\frac{1}{2}m_i\dot{\overrightarrow{r_i}}^2)}{\partial \dot{q_s}})}{dt}-\frac{\partial (\sum\limits_{i=0}^{N}\frac{1}{2}m_i\dot{\overrightarrow{r_i}}^2)}{\partial q_s}$

                $\sum\limits_{i=0}^{N}（m\ddot{\overrightarrow{r}}\cdot\frac{\partial\overrightarrow{r_i}}{\partial q_s})=\frac{d(\frac{\partial T}{\partial \dot{q_s}})}{dt}-\frac{\partial T}{\partial q_s}$

        5. 回归主线式2.4：$\sum\limits_{i=0}^{N}[(\overrightarrow{F_i}-m_i\ddot{\overrightarrow{r_i}})\cdot\frac{\partial\overrightarrow{r_i}}{\partial q_s}]=0$，代入式3、式4:

            1. $\sum\limits_{i=0}^{N}(\overrightarrow{F_i}\cdot\frac{\partial\overrightarrow{r_i}}{\partial q_s})=\sum\limits_{i=0}^{N}(m_i\ddot{\overrightarrow{r_i}}\cdot\frac{\partial\overrightarrow{r_i}}{\partial q_s})$
            2. 得到**拉格朗日方程**：
                1. $Q_s=\frac{d(\frac{\partial T}{\partial \dot{q_s}})}{dt}-\frac{\partial T}{\partial q_s}$
                2. **广义动量**：$P_s=\frac{\partial T}{\partial \dot{q_s}}$
                3. $Q_s=\frac{dP_s}{dt}-\frac{\partial T}{\partial q_s}$

    4. 特殊情况

        1. 牛顿第二定律。取笛卡尔坐标系，$T=\frac{1}{2}m v^2$，$\dot{q_s}=v$，动能和坐标$q$无关所以有一项为0：

            $Q_s=F=\frac{d(mv)}{dt}$

        2. 力学所受的主动力$F_i$全都是保守力（保守力所作的功与路径无关，只与起始位置有关），可以算势能

            1. 势能$U=U(\overrightarrow{r_1},\overrightarrow{r_2},...,\overrightarrow{r_n})$

            2. $\overrightarrow{F_i}=-\frac{\partial U}{\partial \overrightarrow{r_i}}$

            3. $Q_s=\sum\limits_{i=0}^{N}（\overrightarrow{F_i}\cdot\frac{\partial\overrightarrow{r_i}}{\partial q_s}）$

            4. $Q_s=\sum\limits_{i=0}^{N}（-\frac{\partial U}{\partial \overrightarrow{r_i}}\cdot\frac{\partial\overrightarrow{r_i}}{\partial q_s}）$

            5. $Q_s=\frac{\partial U}{\partial  q_s}$

            6. 则拉格朗日方程变为：$-\frac{\partial U}{\partial  q_s}=\frac{d(\frac{\partial T}{\partial \dot{q_s}})}{dt}-\frac{\partial T}{\partial q_s}$

            7. 势能$U$和**广义速度**$\dot{q_s}$无关：

                $0=\frac{d(\frac{\partial (T-U)}{\partial \dot{q_s}})}{dt}-\frac{\partial (T-U)}{\partial q_s}$

            8. **拉格朗日函数**：$L=T-U$

                $0=\frac{d(\frac{\partial (L)}{\partial \dot{q_s}})}{dt}-\frac{\partial (L)}{\partial q_s}$

#### 机器人中的动力学方程（拉格朗日方程）

1. 公式结果
    1. $\tau = M(\theta)\ddot\theta+C(\theta,\dot\theta)+g(\theta)$
    2. $\tau = M(\theta)\ddot\theta+C(\theta,\dot\theta)\dot\theta+g(\theta)$
    3. $\tau = M(\theta)\ddot\theta+\dot\theta\Gamma(\theta)\dot\theta+g(\theta)$
    4. $\tau = M(\theta)\ddot\theta+h(\theta,\dot\theta)$

### 控制

1. 方案1：腿是轻质的，不对腿做动力学分析，将机器人整体进行分析，简化成质点

    1. 确定我们想让机器人实现一个怎么样的运动，即确定向前的位置和速度和加速度
    2. 用牛二，算出机器人质点向前应该需要多大的力
    3. 利用VMC算法，算出机器人的腿末端应该要施加多大的力
    4. 算出雅可比矩阵，解算出机器人的腿的电机需要施加多大的力来达到效果
    5. （其实我觉得应该不是这样）

2. 方案2：还是利用之前的运动学规划，只不过在机器人的腿的末端加上了阻抗控制。这样能用上之前的规划，又有一定鲁棒性

    1. 电机有一个模式：基于电流的位置控制模式

        1. 现象

            1. 设定位置，电机会转
            2. 设定电流，不设定位置，电机不会转
            3. 设定位置，设定小电流，电机慢慢转

        2. 电机说明

            ![image-20210905143132707](RHex%E5%8A%A8%E5%8A%9B%E5%AD%A6.assets/image-20210905143132707-0830601.png)

        3. 理解

            1. 输入想要到的位置，根据PID控制，会输出电流。电机输入多大的电流能输控制，这是电机自己弄好的，不用管。
            2. 我们设定的电流只是起到个限制的作用，超过会截断

    2. 阻抗控制

        1. 控制方法

            <img src="RHex%E5%8A%A8%E5%8A%9B%E5%AD%A6.assets/image-20210905145157301-0830605.png" alt="image-20210905145157301" style="zoom:50%;" />

            1. 括号里第一项是，用机器人动力学算出的，希望达到运动轨迹应该要输出的力。力是算的末端的力。

            2. 括号里第二项是，希望末端模拟出来的质量-阻尼-弹簧系统的效果

                1. 这部分的意思是：要达到这个效果，应该输出这么大的力
                2. 效果：
                    1. 距离目标越远，$Kx$就越大，像弹簧一样要拉过去
                    2. 移动的时候造成阻力，速度越大，给你的阻力就越大
                3. 式子中的$x$其实应该是$x_d-x$
                4. $M$、$B$、$K$是自己设置的，是控制模拟系统的表现的参数
                5. 加速度不常用，所以就不用了，$M$直接设置成0

            3. 末端力算出来后，通过雅可比算出关节的力

            4. 算出关节应该给的力后，根据电机的性能曲线，映射得出电机应该输出的电流（图中的粉红色曲线）

                ![img](RHex%E5%8A%A8%E5%8A%9B%E5%AD%A6.assets/xh540_w270_performance_graph-20210905163008748.jpg)

        2. 实际应用

            1. 运动规划还是用的位置控制
            2. 目标电流$=$限制电流$=f(\tau)=f(\bold J^TF)=f(\bold J^T(C\dot x+K(x_d-x)))$
            3. 如果只有弹簧：目标电流$=$限制电流 $=f(\bold J^T(K(x_d-x)))$
            4. 情况分析
                1. 没有阻力的时候，和位置控制也不一样。
                    1. **可以想象成，一条直线上，质点规划的轨迹是往前走，目标位置和实际位置之间有一根弹簧，目标位置是匀速向前，从而根据弹簧来拉动实际位置。前提是PID原本想输出的电流是大于这个电流限制的**
                    2. 这样永远都有误差，好在电机有PID控制，会矫正
                    3. 当接近目标点的时候，弹簧给的力又很小了，导致电流被限制得很低，基本不动了。目标和实际之间的位置拉远了之后又会动。
                2. 有阻力的时候，阻力会让$x$、$\dot x$发生变化
                    1. 变化得越大，和实际误差也越大，PID会想输出大电流，误差大了同时弹簧限制的电流上限变大了，于是就会产生大的力想弹回去。误差越大力越大，但是在小范围内力是小的，不像正经的位置控制
                3. **其实这种模式下，不设置电流，直接给目标位置，PID也会有一定的柔顺效果**

# 视频展示

见附件
