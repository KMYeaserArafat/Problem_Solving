int countmin = 0;
    int countmax = 0;
    int minimum,maximum; 

    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            if(scores[i]<scores[j+1]){
                minimum = scores[i];
                countmin++;
            }

            if(scores[i]>scores[j+1]){
                maximum = scores[i];
                countmax++;
            }
        }
    }

    cout<<countmax<<" "<<countmin<<endl;