from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class test(Base):
    __tablename__ = 'test'

    appid = Column(Integer, primary_key=True)
    name = Column(String)
    min_specs = Column(Text)
    rec_specs = Column(Text)


class game_requirements(Base):
    __tablename__ = 'game_requirements'

    __bind_key__ = 'project'
    appid = Column(Integer, primary_key=True)
    name = Column(String)
    min_specs = Column(Text)
    rec_specs = Column(Text)
    min_cpu_score = Column(Integer)
    rec_cpu_score = Column(Integer)
    min_gpu_score = Column(Integer)
    _rec_gpu_score = Column(Integer)


class cpubenchmarks(Base):
    __tablename__ = 'cpubenchmarks'

    __bind_key__ = 'project'
    cpu_name = Column(String, primary_key=True)
    benchmark_score = Column(Integer)


class gpubenchmarks(Base):
    __tablename__ = 'gpubenchmarks'

    __bind_key__ = 'project'
    gpu_name = Column(String, primary_key=True)
    benchmark_score = Column(Integer)