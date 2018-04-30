"""this py is operation zip file"""

import zipfile
import os


def read_zipfile(file_path_, file_name_, pwd_=None):
    """
    没有用yeld方法只支持读取小文件.

    :param file_path_: 压缩包路径

    :param file_name_: 文件名

    :param pwd_: 压缩包密码默认为空

    :return zip_files_info:  返回一个字典key为文件全名（路径加文件名）value为文件内容

    """
    _zip = zipfile.ZipFile(file_path_, 'r')
    zip_files_info = {}
    if file_name_ is None:
        for _zipinfo in _zip.filelist:
            if not _zipinfo.is_dir():
                _zipfile = _zip.open(_zipinfo.filename,
                                     pwd=bytes(pwd_, encoding='utf8')
                                     if pwd_ is not None else None)
                zip_files_info[_zipinfo.filename] = _zipfile.read()
    else:
        _zipfile = _zip.open(file_name_,
                             pwd=bytes(pwd_, encoding='utf8')
                             if pwd_ is not None else None)
        zip_files_info[file_name_] = _zipfile.read()
        _zipfile.close()
        _zip.close()
    return zip_files_info


def write_zipfile(file_path_, write_info_, file_name_=None, pwd_=None):
    """
    没有用yeld方法,只支持读取小文件.

    :param file_path_: 压缩包路径

    :param file_name_: 指定某个要写入的文件名或者是一个文件的别名 要看write_info_是不是一个文件

    :param write_info_: 写文件的内容或者是一个文件

    :param pwd_: 压缩包密码默认为空

    """

    if file_name_ is not None:
        if os.path.isfile(write_info_):
            _zip = zipfile.ZipFile(file_path_, 'a')
            _zip.write(write_info_, arcname=os.path.split(file_name_)[1], compress_type=zipfile.zlib.DEFLATED)
            _zip.close()
        elif pwd_ is None:
            _zip = zipfile.ZipFile(file_path_, 'a')
            _zipfile = _zip.getinfo(file_name_)
            _zipWritefile = _zip.open(file_name_, 'r', pwd=bytes(pwd_, encoding='utf8') if pwd_ is not None else None)
            _zip.writestr(_zipfile, _zipWritefile.read() + bytes(write_info_, encoding='utf8'))
            _zipWritefile.close()
            _zip.close()
        elif pwd_ is not None:
            print('不能修改有密码的zip包中的文件内容')
    else:
        if os.path.isfile(write_info_):
            _zip = zipfile.ZipFile(file_path_, 'a')
            _zip.write(write_info_, compress_type=zipfile.zlib.DEFLATED)
            _zip.close()
        else:
            _zip = zipfile.ZipFile(file_path_, 'a')
            for _zipinfo in _zip.filelist:
                if not _zipinfo.is_dir():
                    _zipfile = _zip.open(_zipinfo.filename, 'r',
                                         pwd=bytes(pwd_, encoding='utf8') if pwd_ is not None else None)
                    _zip.writestr(_zipinfo, _zipfile.read() + bytes(write_info_, encoding='utf8'))
                    _zipfile.close()
                    _zip.close()
                    break
                else:
                    continue


def zip_dir(dirname, zipfilename, pwd_=None):
    filelist = []
    if os.path.isfile(dirname):
        filelist.append(dirname)
    else:
        for root, dirs, files in os.walk(dirname):
            for dir in dirs:
                filelist.append(os.path.join(root, dir))
            for name in files:
                filelist.append(os.path.join(root, name))

    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        arcname = tar[len(dirname):]
        zf.write(tar, arcname)
    zf.setpassword(bytes(pwd_, encoding='utf8'))
    zf.close()


def unzip_dir(zipfilename, unzipdirname, pwd_=None):
    fullzipfilename = os.path.abspath(zipfilename)  # 返回zipfilename的绝对路径
    fullunzipdirname = os.path.abspath(unzipdirname)  # 需要解压的目录绝对路径
    if os.path.isfile(fullunzipdirname):
        os.remove(fullunzipdirname)
    elif not os.path.exists(fullunzipdirname):
        os.mkdir(fullunzipdirname)
    srcZip = zipfile.ZipFile(fullzipfilename, "r")
    srcZip.extractall(unzipdirname, pwd=bytes(pwd_, encoding='utf8') if pwd_ is not None else None)


if __name__ == '__main__':  # 此为测试方法
    filename = r'E:\aa.zip'
    dirname = r'D:\Eastmoney\Choice\config\Comm'
    # zip_dir(dirname,filename,pwd_='abc')
    write_info = r'E:\log_network.txt'
    unzipdir = r'E:\aa'
    # write_zipfile(file_path_=filename,file_name_='11.txt',write_info_='213hgjghjdfgd4fgh5gfhf6654')
    unzip_dir(filename, unzipdir)
    # zip_dir(r'D:\eclipse\p2',filename)
