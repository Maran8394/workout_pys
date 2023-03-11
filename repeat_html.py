num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
            90: 'Ninety', 0: 'Zero'}
def n2w(n):
    try:
        return num2words[n]
    except KeyError:
        try:
            return (num2words[n-n%10] + num2words[n%10].lower())
        except KeyError:
            print ('Number out of range')




file = open("file.txt", "w")
for i in range(1,21):
    num = n2w(i)
    print(num)
    t = num.title()

    div = f"""
    <div class="accordion-item mt-3">
        <h2 class="accordion-header" id="heading{t}">
            <button class="accordion-button collapsed " type="button" data-bs-toggle="collapse"
                                    data-bs-target="#collapse{t}" aria-expanded="false" aria-controls="collapse{t}">
                <h6 class="fs-18 m-0 text-uppercase">

                </h6>
            </button>
        </h2>
        <div id="collapse{t}" class="accordion-collapse collapse" aria-labelledby="heading{t}"
                            data-bs-parent="#accordionExample">
            <div class="accordion-body">
                                <h6 class="fs-20 mb-4 text-center text-uppercase">
                                </h6>
                                <p class="fs-16">
                                
                                </p>
                                <ul class="ul-list">
                                
                                </ul>
                                
                </div>
            </div>
    </div>
    """
    file.write(div)
    file.write("\n\n")
