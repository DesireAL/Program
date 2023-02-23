/**************************************/
/*����������S1�ⲿ�жϷ�ʽ�ı�LED1״̬
**************************************/
#include <ioCC2530.h>

#define uint unsigned int
#define uchar unsigned char

//�������LED�ƵĶ˿�
#define LED1 P1_0	//����LED1ΪP1.0�ڿ���
#define KEY1 P0_1       //�жϿ�
//��������
void Delayms(uint);		//��ʱ����
void InitLed(void);		//��ʼ��P1��
void KeyInit();                 //������ʼ��
uchar KeyValue=0;

/****************************
//��ʱ����
*****************************/
void Delayms(uint xms)   //i=xms ����ʱi����
{
 uint i,j;
 for(i=xms;i>0;i--)
   for(j=587;j>0;j--);
}
/****************************
LED��ʼ������
*****************************/
void InitLed(void)
{
  P1DIR |= 0x01; //P1_0����Ϊ���
  LED1 = 1;       //LED1��Ϩ��     
}

/****************************
KEY��ʼ������--�ⲿ�жϷ�ʽ
*****************************/
void InitKey()
{
  P0IEN |= 0X2;  //P01����Ϊ�жϷ�ʽ 
  PICTL |= 0X2; // �½��ش���   
  IEN1 |= 0X20;   // ����P0���ж�; 
  P0IFG = 0x00;   // ��ʼ���жϱ�־λ
  EA = 1; 
}

/**************************** 
      �жϴ����� 
*****************************/ 
#pragma vector = P0INT_VECTOR    //��ʽ��#pragma vector = �ж����������������жϴ������
  __interrupt void P0_ISR(void) 
 { 
  Delayms(10);            //ȥ������
  LED1=~LED1;             //�ı�LED1״̬
  P0IFG = 0;             //���жϱ�־ 
  P0IF = 0;             //���жϱ�־ 
 } 

/***************************
          ������
***************************/
void main(void)
{
	InitLed();		//���ó�ʼ������
	InitKey();
        while(1)
	{
        }
}
