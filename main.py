import argparse
from facerog.Trainer import Trainer
from db import DataBase
from facerog.predict import predict
if __name__ =="__main__":
    db = DataBase()
    trainer = Trainer(db=db)
    args  = argparse.ArgumentParser()
    args.add_argument('-t','--train',type=bool,default=False)
    args.add_argument('-n','--name',type=str,default=None)
    args.add_argument('-p','--predict',type=bool,default=False)
    pargs = args.parse_args()
    print(pargs)
    if pargs.predict:
        predict(db)
    elif pargs.train and pargs.name != None:
        trainer.start_collecting(pargs.name)
    else:
        trainer.retraint_model()

