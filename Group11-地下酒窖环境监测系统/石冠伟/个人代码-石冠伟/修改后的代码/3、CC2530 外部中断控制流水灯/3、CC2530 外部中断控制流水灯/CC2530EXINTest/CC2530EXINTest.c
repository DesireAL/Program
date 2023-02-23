#include <ioCC2530.h>
#define uint  unsigned int
#define uchar unsigned char
//������ƵƵĶ˿�
#define LED1   P1_0	  //����LED1ΪP10�ڿ���
#define LED3   P0_4	  //����LED3ΪP04�ڿ���
#define KEY1   P0_1       //���尴��S1ΪP01�ڿ���
//��������
void Delay(uint);		//��ʱ��������
void Initial(void);		//��ʼ����������
void InitKey(void);             //��ʼ��������������
uchar KeyScan(void);            //����ɨ�躯������

uchar Keyvalue = 0 ;                //���������¼��������
uint  KeyTouchtimes = 0 ;           //���������¼��������
/****************************
//��ʱ
*****************************/
void Delay(uint n)
{
	uint i;
	for(i = 0;i<n;i++);
	for(i = 0;i<n;i++);
	for(i = 0;i<n;i++);
	for(i = 0;i<n;i++);
	for(i = 0;i<n;i++);
        for(i = 0;i<n;i++);
	for(i = 0;i<n;i++);
	for(i = 0;i<n;i++);
	for(i = 0;i<n;i++);
	for(i = 0;i<n;i++);
        for(i = 0;i<n;i++);
	for(i = 0;i<n;i++);
	for(i = 0;i<n;i++);
	for(i = 0;i<n;i++);
	for(i = 0;i<n;i++);
        
}
/****************************
//��ʼ������Ϊ�ж����뷽ʽ
*****************************/
void InitKeyINT(void)
{
  P0INP |= 0x02; //����    
  P0IEN |= 0X02;   //P01����Ϊ�жϷ�ʽ
  PICTL |= 0X01;   //�½��ش���
  EA = 1;
  IEN1 |= 0X20;   // P0����Ϊ�жϷ�ʽ;
  P0IFG |= 0x00;   //��ʼ���жϱ�־λ
  
}
/****************************
//��ʼ������,��P10��P11��P04����Ϊ����ڣ�����LED�Ƴ�ʼ��Ϊ��
*****************************/
void InitIO(void)
{
    P1DIR |= 0x03; //P10��P11����Ϊ���
    P0DIR |= 0x10; //P04����Ϊ���
    LED1 = 1;
    LED3 = 1;	//LED�Ƴ�ʼ��Ϊ��
}
/****************************
//�жϴ�����
*****************************/
#pragma vector = P0INT_VECTOR
 __interrupt void P0_ISR(void)
 {
  if(P0IFG>0)            //�����ж�
  {
    P0IFG = 0;
    Delay(100);  
    if(P0IFG==0)         //�����ж�
    {
      Delay(100);  
      KeyTouchtimes = KeyTouchtimes+1;  //ÿ���жϷ���ʱ��¼����������1
    }  
  }       
  P0IF = 0;             //���жϱ�־
 }
/***************************
//������
***************************/
void main(void)
{
  InitIO();	
  InitKeyINT();               //���ó�ʼ������
   
  while(1)
  {
    if(KeyTouchtimes == 1)       //��������ΪLED3,LED2,LED1������ˮ��˸ 
    {
      LED3 = !LED3;                
      Delay(30000);                    
      LED1 = !LED1;           
      Delay(30000);
      KeyTouchtimes = 0;        
    }
  }
 }