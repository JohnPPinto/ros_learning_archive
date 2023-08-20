// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_robot_interface:msg/TurtleArray.idl
// generated code does not contain a copyright notice

#ifndef MY_ROBOT_INTERFACE__MSG__DETAIL__TURTLE_ARRAY__BUILDER_HPP_
#define MY_ROBOT_INTERFACE__MSG__DETAIL__TURTLE_ARRAY__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "my_robot_interface/msg/detail/turtle_array__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace my_robot_interface
{

namespace msg
{

namespace builder
{

class Init_TurtleArray_turtles
{
public:
  Init_TurtleArray_turtles()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::my_robot_interface::msg::TurtleArray turtles(::my_robot_interface::msg::TurtleArray::_turtles_type arg)
  {
    msg_.turtles = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_robot_interface::msg::TurtleArray msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_robot_interface::msg::TurtleArray>()
{
  return my_robot_interface::msg::builder::Init_TurtleArray_turtles();
}

}  // namespace my_robot_interface

#endif  // MY_ROBOT_INTERFACE__MSG__DETAIL__TURTLE_ARRAY__BUILDER_HPP_
