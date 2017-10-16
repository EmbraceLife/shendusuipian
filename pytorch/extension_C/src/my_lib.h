/* src/my_lib.h */
int my_lib_add_forward(THFloatTensor *input1, THFloatTensor *input2, THFloatTensor *output);
int my_lib_add_backward(THFloatTensor *grad_output, THFloatTensor *grad_input);
int THSize_isSameSizeAs(const int64_t *sizeA, int64_t dimsA, const int64_t *sizeB, int64_t dimsB);
