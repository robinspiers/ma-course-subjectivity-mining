from ml_pipeline import experiment
import argparse

parser = argparse.ArgumentParser(description='run classifier on data')
parser.add_argument('--task', dest='task', default="vua_format")
parser.add_argument('--data_dir', dest='data_dir', default="data/OLID/")
parser.add_argument('--pipeline', dest='pipeline', default='cnn_raw')
parser.add_argument('--print_predictions', dest='print_predictions', default=False)
parser.add_argument('--train_file', dest ='train_file', default = "olid-training-v1.0.tsv")
parser.add_argument('--test_file', dest ='test_file', default = "testA.csv")
parser.add_argument('--save', dest ='save', default = True)
parser.add_argument('--result_file', dest ='result_file', default = "cnn_prep_output.csv")
args = parser.parse_args()


experiment.run(args.task, args.data_dir, args.pipeline, args.print_predictions, args.train_file, args.test_file,
               args.save, args.result_file)
