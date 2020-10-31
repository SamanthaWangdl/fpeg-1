# FPEG

Fudan Photographic Expert Group (FPEG) is a method of lossy compression for digital images developed by Fudan undergraduate students.

This repository is a a python implementation of FPEG and JPEG2000.



## Code Organization

```bash
|   LICENSE
|   README.md
|   source.py
|
\---fpeg
    |   app.py
    |   base.py
    |   config.ini
    |   config.py
    |   fpeg.py
    |   jpeg.py
    |   log.py
    |   monitor.py
    |   pipeline.py
    |   pretty_printer.py
    |   __init__.py
    |
    +---codec
    |       huffman_codec.py
    |       shannon_codec.py
    |       __init__.py
    |
    +---metrics
    |       __init__.py
    |
    +---processor
    |       __init__.py
    |
    +---test
    |       __init__.py
    |
    +---transformer
    |       __init__.py
    |
    +---utils
            io.py
            lut.py
            __init__.py

```



## To Contribute

Codecs, transformers, processors are all pipes in FPEG. 

A certain codec, like huffman codec, is a subclass of Pipe (and Codec). To implement a codec is to implement the \_\_init\_\_, encode and decode methods. Put what the codec need and what the monitor should know in \_\_init\_\_'s signature, such as Look Up Table (LUT) and Define Huffman Table (DHT) for encoding and decoding. After that, you can set what should not be known by monitor, such as its log and logger.

In encode and decode methods, the codec should first clear its history information, i.e. the LUTs and DHTs used in processing former data, using self._clear_record method. Moreover, encode and decode methods should support parallel computing using python’s implementation subprocess pool (self.pool). **Refer to the code of HuffmanCodec for more information and follow a unified code specification** (*make other codec similar to HuffmanCodec !!!*).

Now you should only implement Codecs. Transformer, processor, metrics, monitor and pipeline’s form are not completely sure yet.

 

## TODOs

- [ ] Codecs
	- [ ] Huffman encoding
- [ ] Shannon encoding
- [ ] Transformers
	- [ ] DWT and IDWT transformer
	- [ ] FFT and IFFT transformer
- [ ] Processors
	- [ ] Block divider
- [ ] IO
	- [ ] Reader
	- [ ] Writer
- [ ] Utils
	- [ ] dht2lht
- [ ] Metrics
- [ ] Monitor
- [ ] Pipeline