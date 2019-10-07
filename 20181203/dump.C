void dump(TString filename) {

  ifstream deadchannelfile;

  Int_t bla = 0;
  Int_t side = 0;
  Int_t sector = 0;
  Int_t partition = 0;
  Int_t hwaddr = 0;
  Int_t amp = 0;

  deadchannelfile.open(filename.Data());

  if ( deadchannelfile.is_open() ) {

    deadchannelfile >> bla; // read first number

    while (deadchannelfile >> bla >> side >> sector >> partition >> hwaddr >> amp) {
      Int_t branch  = (hwaddr>>11)&0x1;
      Int_t fec     = (hwaddr>> 7)&0xF;
      Int_t altro   = (hwaddr>> 4)&0x7;
      Int_t channel = (hwaddr>> 0)&0xF;
      cout << "side " << side << ", sector " << sector << ", partition " << partition << ", branch " << branch
	   << ", fec " << fec << ", altro " << altro << ", channel " << channel << endl;
    }
    deadchannelfile.close();

  } else
    cerr << "Error opening file " << filename[i] << endl;

}
