#include <stdio.h>
#include <math.h>
#include <complex.h>
#include <fftw3.h>

#define N 1001
#define xlim 100

double gaussian(double x) {
    return exp(-x*x);
}

int main() {
    fftw_complex in[N], out[N];
    fftw_plan p;
    double delta = (double) 2 * xlim / (N - 1);

    p = fftw_plan_dft_1d(N, in, out, FFTW_FORWARD, FFTW_ESTIMATE);

    for (int i=0; i < N; i++) {
        in[i] = gaussian(-xlim + i * delta) + I * 0.0;
    }

    fftw_execute(p);

    FILE *file = fopen("q4_data.csv","w");

    for (int i = 0; i < N; i++) {
        fprintf(file, "%g, %g\n", creal(out[i]), cimag(out[i]));
    }

    fclose(file);

    fftw_destroy_plan(p);
    fftw_cleanup();

    printf("Fourier transform data has been written to 'q4_data.csv'.\n");

    return 0;
}