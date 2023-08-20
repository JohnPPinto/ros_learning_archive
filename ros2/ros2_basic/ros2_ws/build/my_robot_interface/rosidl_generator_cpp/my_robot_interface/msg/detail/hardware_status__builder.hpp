// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_robot_interface:msg/HardwareStatus.idl
// generated code does not contain a copyright notice

#ifndef MY_ROBOT_INTERFACE__MSG__DETAIL__HARDWARE_STATUS__BUILDER_HPP_
#define MY_ROBOT_INTERFACE__MSG__DETAIL__HARDWARE_STATUS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "my_robot_interface/msg/detail/hardware_status__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace my_robot_interface
{

namespace msg
{

namespace builder
{

class Init_HardwareStatus_debug_message
{
public:
  explicit Init_HardwareStatus_debug_message(::my_robot_interface::msg::HardwareStatus & msg)
  : msg_(msg)
  {}
  ::my_robot_interface::msg::HardwareStatus debug_message(::my_robot_interface::msg::HardwareStatus::_debug_message_type arg)
  {
    msg_.debug_message = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_robot_interface::msg::HardwareStatus msg_;
};

class Init_HardwareStatus_are_motors_ready
{
public:
  explicit Init_HardwareStatus_are_motors_ready(::my_robot_interface::msg::HardwareStatus & msg)
  : msg_(msg)
  {}
  Init_HardwareStatus_debug_message are_motors_ready(::my_robot_interface::msg::HardwareStatus::_are_motors_ready_type arg)
  {
    msg_.are_motors_ready = std::move(arg);
    return Init_HardwareStatus_debug_message(msg_);
  }

private:
  ::my_robot_interface::msg::HardwareStatus msg_;
};

class Init_HardwareStatus_temperature
{
public:
  Init_HardwareStatus_temperature()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_HardwareStatus_are_motors_ready temperature(::my_robot_interface::msg::HardwareStatus::_temperature_type arg)
  {
    msg_.temperature = std::move(arg);
    return Init_HardwareStatus_are_motors_ready(msg_);
  }

private:
  ::my_robot_interface::msg::HardwareStatus msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_robot_interface::msg::HardwareStatus>()
{
  return my_robot_interface::msg::builder::Init_HardwareStatus_temperature();
}

}  // namespace my_robot_interface

#endif  // MY_ROBOT_INTERFACE__MSG__DETAIL__HARDWARE_STATUS__BUILDER_HPP_
