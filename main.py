from remot_control_lap import*


def main():
    app = QApplication([])
    window = Controller()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()