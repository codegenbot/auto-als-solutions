float truncate_number(float number) {
    return modf(number, &intPart)->rd;
}