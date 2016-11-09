import csv

class Database:
    def __init__(self, dbase_filename="data.csv"):
        self.dbase_filename = dbase_filename
        self.users = {}
        with open(self.dbase_filename, "r") as f:
            for line in f:
                new_line = line.split(",")
                self.users[new_line[0]] = new_line

    def __getitem__(self, username):
        for line in self.users:
            if line[username] == username:
                return line

    def add(self, new_user):
        self.users[new_user[0]] = new_user
        self._save()

    def __repr__(self):
        return str(self.users)

    def _save(self):
        with open("data.csv", "w") as f:
            for key in self.users:
                f.write(",".join(self.users[key]))
                f.write("\n")

if __name__ == '__main__':
    pass
