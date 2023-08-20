// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_robot_interface:msg/LedStatus.idl
// generated code does not contain a copyright notice

#ifndef MY_ROBOT_INTERFACE__MSG__DETAIL__LED_STATUS__BUILDER_HPP_
#define MY_ROBOT_INTERFACE__MSG__DETAIL__LED_STATUS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "my_robot_interface/msg/detail/led_status__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace my_robot_interface
{

namespace msg
{

namespace builder
{

class Init_LedStatus_led_panel_state
{
public:
  Init_LedStatus_led_panel_state()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::my_robot_interface::msg::LedStatus led_panel_state(::my_robot_interface::msg::LedStatus::_led_panel_state_type arg)
  {
    msg_.led_panel_state = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_robot_interface::msg::LedStatus msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_robot_interface::msg::LedStatus>()
{
  return my_robot_interface::msg::builder::Init_LedStatus_led_panel_state();
}

}  // namespace my_robot_interface

#endif  // MY_ROBOT_INTERFACE__MSG__DETAIL__LED_STATUS__BUILDER_HPP_
