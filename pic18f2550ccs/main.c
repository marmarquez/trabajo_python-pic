#include <main.h>

#byte porta = 0xf80 // Identificador para el puerto A. 
#byte portb = 0xf81 // Identificador para el puerto B. 
//#byte portc = 0xf82 // Identificador para el puerto C. 
//#byte portd = 0xf83 // Identificador para el puerto D. 
//#byte porte = 0xf84 // Identificador para el puerto E.
 
//#define  USB_CONFIG_PID       0x000A
//#define  USB_CONFIG_VID       0x04D8
 
// if USB_CDC_ISR is defined, then this function will be called
// by the USB ISR when there incoming CDC (virtual com port) data.
// this is useful if you want to port old RS232 code that was use
// #int_rda to CDC.
#define USB_CDC_ISR() RDA_isr()
 
// in order for handle_incoming_usb() to be able to transmit the entire
// USB message in one pass, we need to increase the CDC buffer size from
// the normal size and use the USB_CDC_DELAYED_FLUSH option.
// failure to do this would cause some loss of data.
//#define USB_CDC_DELAYED_FLUSH 
#define USB_CDC_DATA_LOCAL_SIZE  128
 
static void RDA_isr(void);

// Includes all USB code and interrupts, as well as the CDC API
#include <usb_cdc.h>
#include <stdlib.h>
#include <string.h>

 
// #define USB_CON_SENSE_PIN PIN_B2 //No usado cuando alimentado desde el USB
#define LED1 PIN_B4
#define LED2 PIN_B5
 
int deg=0;
 
//Define la interrupción por recepción Serial
static void RDA_isr(void)
{  
 while(usb_cdc_kbhit())
   {
    // int i=0,ini=0,fin=0;
    char dat[1];

    dat[0] = usb_cdc_getc();
        
    if(dat[0] == 'N')
      output_toggle(LED1);
      
    }
 }
 
 
void main(){   
   
   set_tris_b(0b00000100);
   //bit_clear(portb,4);
   //bit_clear(portb,5);
 
   usb_cdc_init();
   usb_init();
   
   //enable_interrupts(INT_RDA); //Habilita Interrupción por serial (Recepcion USB_CDC)
   //enable_interrupts(GLOBAL);  //Habilita todas las interrupciones
   
   while(true){
      usb_task();  //Verifica la comunicación USB
      if(usb_enumerated()) {
         output_toggle(LED2);
         delay_ms(1000);
      }
   }
}
