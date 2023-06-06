from rclpy.node import Node
from typing import Any

class Subscription:
	def __init__(self, name: str, node: Node, srv_name: str, srv_type: Any, custom_qos: Any = None):
		# Setup instance variables
		self.name = name
		self.node = node
		self.srv_type = srv_type
		self.srv_name = srv_name
		self.subscription = None
		self.custom_qos = custom_qos
		self.node.get_logger().info(f"Subscription {self.name} created.")

	def connect(self, subscription_callback: Any) -> None:
		self.subscription = self.node.create_subscription(
			self.srv_type, self.srv_name, subscription_callback, self.custom_qos if self.custom_qos is not None else 10
		)  # Create the subscription to the topic with the callback

		self.node.get_logger().info(f"Subscription {self.name} connected.")

	def disconnect(self) -> None:
		self.subscription.destroy()
		self.node.get_logger().info(f"Subscription {self.name} disconnected.")