import abc

class Compression(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def compress_file(self, path):
        pass


class ZIPCompression(Compression):

    def compress_file(self, path):
        print('create zip archive with file: ', path)


class RARCompression(Compression):

    def compress_file(self, path):
        print('create rar archive with file: ', path)


class ARJCompression(Compression):

    def compress_file(self, path):
        print('create arj archive with file: ', path)


class Compressor:

    def __init__(self, compression):
        self._compression = compression

    def compress_file(self, path):
        self._compression.compress_file(path)


def main():
    path_to_file = 'test_compress.txt'
    compression = ZIPCompression()
    compressor = Compressor(compression)
    compressor.compress_file(path_to_file)


if __name__ == "__main__":
    main()