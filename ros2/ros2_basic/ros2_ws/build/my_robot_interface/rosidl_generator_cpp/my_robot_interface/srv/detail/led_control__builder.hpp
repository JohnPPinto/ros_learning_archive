// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_robot_interface:srv/LedControl.idl
// generated code does not contain a copyright notice

#ifndef MY_ROBOT_INTERFACE__SRV__DETAIL__LED_CONTROL__BUILDER_HPP_
#define MY_ROBOT_INTERFACE__SRV__DETAIL__LED_CONTROL__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "my_robot_interface/srv/detail/led_control__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace my_robot_interface
{

namespace srv
{

namespace builder
{

class Init_LedControl_Request_state
{
public:
  explicit Init_LedControl_Request_state(::my_robot_interface::srv::LedControl_Request & msg)
  : msg_(msg)
  {}
  ::my_robot_interface::srv::LedControl_Request state(::my_robot_interface::srv::LedControl_Request::_state_type arg)
  {
    msg_.state = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_robot_interface::srv::LedControl_Request msg_;
};

class Init_LedControl_Request_led_number
{
public:
  Init_LedControl_Request_led_number()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_LedControl_Request_state led_number(::my_robot_interface::srv::LedControl_Request::_led_number_type arg)
  {
    msg_.led_number = std::move(arg);
    return Init_LedControl_Request_state(msg_);
  }

private:
  ::my_robot_interface::srv::LedControl_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_robot_interface::srv::LedControl_Request>()
{
  return my_robot_interface::srv::builder::Init_LedControl_Request_led_number();
}

}  // namespace my_robot_interface


namespace my_robot_interface
{

namespace srv
{

namespace builder
{

class Init_LedControl_Response_success
{
public:
  Init_LedControl_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::my_robot_interface::srv::LedControl_Response success(::my_robot_interface::srv::LedControl_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_robot_interface::srv::LedControl_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_robot_interface::srv::LedControl_Response>()
{
  return my_robot_interface::srv::builder::Init_LedControl_Response_success();
}

}  // namespace my_robot_interface

#endif  // MY_ROBOT_INTERFACE__SRV__DETAIL__LED_CONTROL__BUILDER_HPP_
