# Compare Version Numbers

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        list_ver_1 = version1.split(".")
        list_ver_2 = version2.split(".")

        x = abs(len(list_ver_1) - len(list_ver_2))
        if len(list_ver_1) > len(list_ver_2):
            for _ in range(x):
                list_ver_2.append(0)
        elif len(list_ver_1) < len(list_ver_2):
            for _ in range(x):
                list_ver_1.append(0)

        for i in range(len(list_ver_1)):
            if int(list_ver_1[i]) > int(list_ver_2[i]):
                return 1
            elif int(list_ver_1[i]) < int(list_ver_2[i]):
                return -1
        return 0
