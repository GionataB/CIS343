;;the function takes inputs (numbers) until the user types a negative number, and returns the flat total. (no taxes included)
;;NOTE: This function is out of date, show_total_taxes does the same and much more. Use this only to have a simple output.
(define (show_total)
  (define (pos) ;; function that keeps asking the user for a value, and returns the total.
    (display "Enter: ")
    (let ((x (read)))
      (if (<= x 0) ;;The function takes ONLY positive values, or zero. inputting any negative value will stop the program.
        '0
        (+ (pos) x)
      )
    )
  )
  (display (pos)) ;;Display the value returned from the pos function.
  '0 ;;If it returns 0, there was no problem in the execution
)

(define taxes 0.065) ;;The tax rate used by show_total_taxes

;;the function takes inputs (numbers) until the user types a negative number, and returns the total, and the total with taxes factored in.
(define (show_total_taxes)
  (define (pos) ;;Function that keeps asking the user for a value, and returns the total.
    (display "Enter: $")
    (let ((x (read)))
      (newline)
      (if (<= x 0) ;;The function takes ONLY positive values, or zero. inputting any negative value will stop the program.
        '0
        (+ (pos) x)
      )
    )
  )
  (display "Start transaction (exit with 0 or lower):")
  (newline) (newline)
  (let ((x (pos)))
    (display "Subtotal: $") (write x) ;;Display the total minus taxes
    (newline)
    (display "Tax: ") (write (* taxes 100)) (display "%") ;;Display the taxes as a percentage
    (newline)
    (display "Total: $") (write(/ (floor(* (+ x (* x taxes)) 100)) 100)) ;;Display the total plus taxes, with a max of two decimal digits.
  )
  '0 ;;If it returns 0, there was no problem in the execution
)

(newline) ;; If the user loads the file using the (load) function, this prevents having the load function message on the same line as the pos first message
(show_total_taxes)
