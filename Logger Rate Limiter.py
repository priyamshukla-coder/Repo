class Logger:

    def __init__(self):
        
        self.d1 = defaultdict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:

        if message not in self.d1:

            self.d1[message] = timestamp

            return True

        else:

            # print(self.d1[message])

            if timestamp - self.d1[message] >= 10:

                self.d1[message] = timestamp

                return True

            else:

                return False

        # return True


        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)