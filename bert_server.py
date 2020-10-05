from bert_serving.server.helper import get_args_parser
import sys

from bert_serving.server import BertServer


if __name__ == '__main__':
    args = get_args_parser().parse_args(['-model_dir', '/home/sduser/project/linebot/chinese_L-12_H-768_A-12',
                                         '-num_worker', '2'])
    server = BertServer(args)
    server.start()
