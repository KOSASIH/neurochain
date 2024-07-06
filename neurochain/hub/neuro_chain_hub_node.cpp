#include <ros/ros.h>
#include <neuro_chain_hub/neuro_chain_hub.h>

int main(int argc, char **argv) {
    ros::init(argc, argv, "neuro_chain_hub_node");
    ros::NodeHandle nh;
    NeuroChainHub hub;
    hub.init();
    ros::spin();
    return 0;
}
