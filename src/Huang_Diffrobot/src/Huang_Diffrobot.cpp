#include <cstdio>
#include <rclcpp/rclcpp.hpp>
#include <memory>
#include <geometry_msgs/msg/twist.hpp>
#include <chrono>
#include <string>
#include <functional>

using namespace std::chrono_literals;
int main(int argc, char ** argv)
{
  (void) argc;
  (void) argv;
  //初始化节点
  rclcpp::init(argc, argv);
  //节点名
  std::shared_ptr<rclcpp::Node> node =
    std::make_shared<rclcpp::Node>("huang_diffrobot");
  //创建发布者
  auto publisher = node->create_publisher<geometry_msgs::msg::Twist>(
    "/diff_drive_base_controller/cmd_vel_unstamped", 10);
  float linear_x,linear_y,linear_z,angular_x,angular_y,angular_z;
  
  node->declare_parameter<float>("linear_x", 0);
  node->declare_parameter<float>("linear_y", 0);
  node->declare_parameter<float>("linear_z", 0);
  node->declare_parameter<float>("angular_x", 0);
  node->declare_parameter<float>("angular_y", 0);
  node->declare_parameter<float>("angular_z", 0);
  //获取参数名字为name的值
  node->get_parameter<float>("linear_x", linear_x);
  node->get_parameter<float>("linear_y", linear_y);
  node->get_parameter<float>("linear_z", linear_z);
  node->get_parameter<float>("angular_x", angular_x);
  node->get_parameter<float>("angular_y", angular_y);
  node->get_parameter<float>("angular_z", angular_z);
  geometry_msgs::msg::Twist command;

  command.linear.x = linear_x;
  command.linear.y = linear_y;
  command.linear.z = linear_z;

  command.angular.x = angular_x;
  command.angular.y = angular_y;
  command.angular.z = angular_z;

  while (1) {
    publisher->publish(command);
    std::this_thread::sleep_for(50ms);
    rclcpp::spin_some(node);
  }
  rclcpp::shutdown();

  return 0;
}


