module specialized_mutiplier(SW, HEX);
input [3:0] SW;
output [6:0] HEX;
reg [6:0] HEX;
always @(SW)
    begin
        case(SW)
            4'b0000:HEX <= 7'b1000000;
            4'b0001:HEX <= 7'b1111001;
            4'b0010:HEX <= 7'b0100100;
            4'b0011:HEX <= 7'b1111000;
            4'b0100:HEX <= 7'b0010000;
            4'b0101:HEX <= 7'b0000011;
            4'b0110:HEX <= 7'b0000011;
            4'b0111:HEX <= 7'b0100001;
            4'b1000:HEX <= 7'b0001110;
            default:HEX <= 7'b1000000;
        endcase
    end
endmodule