// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from my_robot_interface:msg/LedStatus.idl
// generated code does not contain a copyright notice

#ifndef MY_ROBOT_INTERFACE__MSG__DETAIL__LED_STATUS__TRAITS_HPP_
#define MY_ROBOT_INTERFACE__MSG__DETAIL__LED_STATUS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "my_robot_interface/msg/detail/led_status__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace my_robot_interface
{

namespace msg
{

inline void to_flow_style_yaml(
  const LedStatus & msg,
  std::ostream & out)
{
  out << "{";
  // member: led_panel_state
  {
    if (msg.led_panel_state.size() == 0) {
      out << "led_panel_state: []";
    } else {
      out << "led_panel_state: [";
      size_t pending_items = msg.led_panel_state.size();
      for (auto item : msg.led_panel_state) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const LedStatus & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: led_panel_state
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.led_panel_state.size() == 0) {
      out << "led_panel_state: []\n";
    } else {
      out << "led_panel_state:\n";
      for (auto item : msg.led_panel_state) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const LedStatus & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace my_robot_interface

namespace rosidl_generator_traits
{

[[deprecated("use my_robot_interface::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const my_robot_interface::msg::LedStatus & msg,
  std::ostream & out, size_t indentation = 0)
{
  my_robot_interface::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use my_robot_interface::msg::to_yaml() instead")]]
inline std::string to_yaml(const my_robot_interface::msg::LedStatus & msg)
{
  return my_robot_interface::msg::to_yaml(msg);
}

template<>
inline const char * data_type<my_robot_interface::msg::LedStatus>()
{
  return "my_robot_interface::msg::LedStatus";
}

template<>
inline const char * name<my_robot_interface::msg::LedStatus>()
{
  return "my_robot_interface/msg/LedStatus";
}

template<>
struct has_fixed_size<my_robot_interface::msg::LedStatus>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<my_robot_interface::msg::LedStatus>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<my_robot_interface::msg::LedStatus>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // MY_ROBOT_INTERFACE__MSG__DETAIL__LED_STATUS__TRAITS_HPP_
