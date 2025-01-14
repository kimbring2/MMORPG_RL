/*
 Copyright (C) 2016 by Wojciech Jaśkowski, Michał Kempka, Grzegorz Runc, Jakub Toczek, Marek Wydmuch

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in
 all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 THE SOFTWARE.
*/

#include "viz_message_queue.h"

bip::message_queue *vizMQController = nullptr;
bip::message_queue *vizMQGolf = nullptr;
char *vizMQControllerName;
char *vizMQGolfName;

void VIZ_MQInit(const char * id){
    //printf("VIZ_MQInit: Init message queues.\n");

	vizMQControllerName = new char[strlen(VIZ_MQ_NAME_CTR_BASE) + strlen(id) + 1];
	strcpy(vizMQControllerName, VIZ_MQ_NAME_CTR_BASE);
	strcat(vizMQControllerName, id);

	vizMQGolfName = new char[strlen(VIZ_MQ_NAME_GOLF_BASE) + strlen(id) +1];
	strcpy(vizMQGolfName, VIZ_MQ_NAME_GOLF_BASE);
	strcat(vizMQGolfName, id);

    //vizMQControllerName = id_2;
    //vizMQGolfName = id_1;

    //printf("client vizMQControllerName: %s\n", vizMQControllerName);
    //printf("client vizMQGolfName: %s\n", vizMQGolfName);

    try {
        vizMQController = new bip::message_queue(bip::open_only, vizMQControllerName);//, VIZ_MQ_MAX_MSG_NUM, VIZ_MQ_MAX_MSG_SIZE);
        vizMQGolf = new bip::message_queue(bip::open_only, vizMQGolfName);//, VIZ_MQ_MAX_MSG_NUM, VIZ_MQ_MAX_MSG_SIZE);
    }
    catch(...) { // bip::interprocess_exception
        //printf("Failed to open message queues.\n");
        throw;
    }
}


void VIZ_MQSend(uint8_t code, const char *command){
    VIZMessage msg;
    msg.code = code;
    if(command) strncpy(msg.command, command, VIZ_MQ_MAX_CMD_LEN);

    if(vizMQController) vizMQController->send(&msg, sizeof(VIZMessage), 0);
}


void VIZ_MQReceive(void *msg) {
    size_t size;
    unsigned int priority;

    if(vizMQGolf) vizMQGolf->receive(msg, sizeof(VIZMessage), size, priority);
}


bool VIZ_MQTryReceive(void *msg){
    size_t size;
    unsigned int priority;

    return vizMQGolf->try_receive(msg, sizeof(VIZMessage), size, priority);
}


void VIZ_MQTic(){
    VIZMessage msg;

    do {
        //if(!*viz_async) VIZ_MQReceive(&msg);
        //else if(!VIZ_MQTryReceive(&msg)) break;
        VIZ_MQReceive(&msg);

        switch(msg.code){
            case VIZ_MSG_CODE_TIC :
                //vizNextTic = true;
                break;

            case VIZ_MSG_CODE_UPDATE:
                //VIZ_Update();
                //VIZ_GameStateTic();
                //VIZ_MQSend(VIZ_MSG_CODE_DOOM_DONE);
                break;

            case VIZ_MSG_CODE_TIC_AND_UPDATE:
                //vizUpdate = true;
                //vizNextTic = true;
                break;

            case VIZ_MSG_CODE_COMMAND:
                //if(msg.command[0] != '\0') VIZ_Command(strdup(msg.command));
                //VIZ_CVARsUpdate();
                break;

            case VIZ_MSG_CODE_CLOSE:
            case VIZ_MSG_CODE_ERROR:
                //D_ClearAll();
                exit(0);

            default : break;
        }
    } while(!false);
}


void VIZ_MQClose(){
    //bip::message_queue::remove(vizMQControllerName);
    //bip::message_queue::remove(vizMQDoomName);
    delete vizMQController;
    delete vizMQGolf;
	delete[] vizMQControllerName;
	delete[] vizMQGolfName;
}
