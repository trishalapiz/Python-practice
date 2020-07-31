using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace TrishaStudentSIMS2.Models
{
    public class Address
    {
        [Key]
        public int addressId { get; set; }
        public int streetNumber { get; set; }
        public string street { get; set; }
        public string suburb { get; set; }
        public string city { get; set; }
        public int postCode { get; set; }
        public string country { get; set; }

        [Required, ForeignKey("Student")] // 1 student can have many addresses, therefore not database generated
        public int studentID { get; set; }
        public Student Student { get; set; }
    }
}