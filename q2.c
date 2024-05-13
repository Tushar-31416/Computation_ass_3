#include <stdio.h>
#include <math.h>
#include <complex.h>
#include <fftw3.h>

#define N 200
#define xmin -50
#define xmax 50

double sinc(double x) {
    if (x == 0.0){
        return 1.0;
    } else {
        return sin(x)/x;
    }
}

int main() {
    double delta = (double) (xmax - xmin) / (N - 1);
    fftw_complex func[N], dft[N];
    fftw_plan fp;
    
    for (int i=0; i < N; i++) {
        func[i] = sinc(xmin + i * delta) + I * 0.0;
    }

    fp = fftw_plan_dft_1d(N,func,dft,FFTW_FORWARD,FFTW_ESTIMATE);
    fftw_execute(fp);
    FILE *file = fopen("q2_data.csv","w");

    for (int i = 0; i < N; i++) {
        fprintf(file, "%g, %g\n", creal(dft[i]), cimag(dft[i]));
    }
    fclose(file);

    fftw_destroy_plan(fp);
    fftw_cleanup();
    return 0;
}
