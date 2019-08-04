import bisect


class SnapshotArray:

    def __init__(self, length: int):
        self.array = {}
        self.snaps = []

    def set(self, index: int, val: int):
        self.array[index] = val

    def snap(self):
        self.snaps.append(self.array.copy())
        return len(self.snaps) - 1

    def get(self, index: int, snap_id: int):
        if index in self.snaps[snap_id]:
            return self.snaps[snap_id][index]
        else:
            return 0


if __name__ == "__main__":

    # Your SnapshotArray object will be instantiated and called as such:
    length = 3
    obj = SnapshotArray(length)
    # set(index, val)
    obj.set(0, 5)
    param_2 = obj.snap()
    param_3 = obj.get(index=0, snap_id=0)
