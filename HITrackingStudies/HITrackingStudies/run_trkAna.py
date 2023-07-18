import FWCore.ParameterSet.Config as cms

process = cms.Process('TRACKANA')
process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True),
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('trk.root')
)

# Input source
process.source = cms.Source("PoolSource",
    duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
    fileNames =  cms.untracked.vstring('file:/afs/cern.ch/work/m/mnguyen/public/prod/CMSSW_12_5_2/src/rawprime/raw_RAW2DIGI_L1Reco_RECO.root')
    # fileNames =  cms.untracked.vstring('file:/eos/cms/store/group/phys_heavyions/mnguyen/rawprime/raw_RAW2DIGI_L1Reco_RECO.root')
)

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2022_realistic_hi', '')
###

#forest style analyzers (anaTrack module) (not affected by HITrackCorrections code)
process.load('HITrackingStudies.AnalyzerCode.trackAnalyzer_cff')
process.anaTrack.doSimVertex = False
process.anaTrack.doMVA = False
process.anaTrack.doSimTrack = False
###

process.p = cms.Path(
                      process.anaTrack
)
