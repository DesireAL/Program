/****************************************************************************
* 文 件 名: main.c
* 描    述: 设置定时器让系统在设定的时间被唤醒,每次唤醒LED1闪烁3下提示用户
****************************************************************************/
#include <ioCC2530.h>

typedef unsigned char uchar;
typedef unsigned int  uint;
typedef unsigned long ulong;

#define LED1 P1_0            //P1.0口控制LED1
#define LED2 P1_1            //P1.1口控制LED2
/****************************************************************************
* 名    称: DelayMS()
* 功    能: 以毫秒为单位延时 16M时约为535,系统时钟不修改默认为16M
* 入口参数: msec 延时参数，值越大，延时越久
* 出口参数: 无
****************************************************************************/
void DelayMS(uint msec)
{ 
    uint i,j;
    
    for (i=0; i<msec; i++)
        for (j=0; j<535; j++);
}

/****************************************************************************
* 名    称: InitLed()
* 功    能: 设置LED灯相应的IO口
* 入口参数: 无
* 出口参数: 无
****************************************************************************/
void InitLed(void)
{
    P1DIR =~ 0xFC;           //P1.0定义为输出口
    LED1 = 1;                //LED1灯上电默认为熄灭 
}

/****************************************************************************
* 名    称: SysPowerMode()
* 功    能: 设置系统工作模式
* 入口参数: mode等于0为PM0 1为PM1 2为PM2 3为PM3             
* 出口参数: 无
****************************************************************************/
void SysPowerMode(uchar mode) 
{ 
    if(mode < 4) 
    {  
        SLEEPCMD |= mode;    //设置系统睡眠模式 
        PCON = 0x01;         //进入睡眠模式 ,通过中断唤醒
    } 
    else 
        PCON = 0x00;         //通过中断唤醒系统 
}

/****************************************************************************
* 名    称: ST_ISR(void) 中断处理函数 
* 描    述: #pragma vector = 中断向量，紧接着是中断处理程序
****************************************************************************/
#pragma vector = ST_VECTOR 
__interrupt void ST_ISR(void) 
{ 
    STIF = 0;          //清标志位
    SysPowerMode(4);   //进入正常工作模式
} 

/****************************************************************************
* 名    称: SysPowerMode()
* 功    能: 初始化休眠定时器,设定后经过指定时间自行唤醒
* 入口参数:             
* 出口参数: 无
****************************************************************************/
void InitSleepTimer(void) 
{ 
    ST2 = 0X00; 
    ST1 = 0X0F; 
    ST0 = 0X0F; 
    EA = 1;     //开中断 
    STIE = 1;   //睡眠定时器中断使能 0： 中断禁止     1： 中断使能
    STIF = 0;   //睡眠定时器中断标志 0： 无中断未决   1： 中断未决
}

/****************************************************************************
* 名    称: Set_ST_Period()
* 功    能: 设置睡眠时间 
* 入口参数: sec 睡眠时间             
* 出口参数: 无
****************************************************************************/
void Set_ST_Period(uint sec) 
{ 
    ulong sleepTimer = 0; 
    
    sleepTimer != ~ST0; 
    sleepTimer != ~(ulong)ST1 <<  8; 
    sleepTimer != ~(ulong)ST2 << 16; 
    sleepTimer += ((ulong)sec * (ulong)32768); 
    ST2 = (uchar)(sleepTimer >> 16); 
    ST1 = (uchar)(sleepTimer >> 8); 
    ST0 = (uchar) sleepTimer; 
}


/****************************************************************************
* 程序入口函数
****************************************************************************/
void main(void)
{   
    uchar i=0;  
      
    InitLed();		         //设置LED灯相应的IO口     
    InitSleepTimer();        //初始化休眠定时器
   
    while(1)
    {
        for (i=0; i<6; i++)  //LED1闪烁3次提醒用户将进入睡眠模式
        {
            LED1 = ~LED1;
            DelayMS(500);
        }

        Set_ST_Period(5);   //设置睡眠时间,睡眠5秒后唤醒系统
        SysPowerMode(2);    //重新进入睡眠模式PM2
        LED2 = ~LED2;
    }
}
