#import datetime
from typing import TypedDict

### A test state
class BaseState(TypedDict):
	namespace: str
	service_account_name: str
