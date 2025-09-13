from abc import ABC, abstractmethod
import threading

# father class
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        pass

# the specific payment type
class CreditCard(PaymentMethod):
    def pay(self, amount: float) -> str:
        return f"[CreditCard] charged ${amount:.2f}"

class PayPal(PaymentMethod):
    def pay(self, amount: float) -> str:
        return f"[PayPal] charged ${amount:.2f}"

class BankTransfer(PaymentMethod):
    def pay(self, amount: float) -> str:
        return f"[BankTransfer] transferred ${amount:.2f}"

class CryptoPayment(PaymentMethod):
    def pay(self, amount: float) -> str:
        return f"[Crypto] sent ${amount:.2f} (crypto equivalent)"

class GooglePay(PaymentMethod):
    def pay(self, amount: float) -> str:
        return f"[GooglePay] charged ${amount:.2f}"

# factory creat logic
class PaymentFactory:
    _registry = {
        "creditcard": CreditCard,
        "paypal": PayPal,
        "banktransfer": BankTransfer,
        "crypto": CryptoPayment,
        "googlepay": GooglePay,
    }

    @classmethod
    def create(cls, method_name: str) -> PaymentMethod:
        key = method_name.strip().lower()
        if key not in cls._registry:
            raise ValueError(f"Unsupported payment method: {method_name}")
        return cls._registry[key]()
# keep singleton
class PaymentGateway:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance: # double check to prevent two request enter in the same time
                    cls._instance = super().__new__(cls)
        return cls._instance

    def process(self, method_name: str, amount: float) -> str:
        method = PaymentFactory.create(method_name)
        return method.pay(amount)


if __name__ == "__main__":
    gw1 = PaymentGateway()
    gw2 = PaymentGateway()
    print("Singleton?", gw1 is gw2)

    print(gw1.process("CreditCard", 19.99))
    print(gw1.process("PayPal", 9.90))
    print(gw1.process("BankTransfer", 100.0))
    print(gw1.process("Crypto", 5.5))
    print(gw1.process("GooglePay", 12.34))
